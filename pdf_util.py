from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO


def convert_pdf_to_txt_as_pages(path):
    """
    returns a list, in order, of all pages start to finish
    :param path: string path to your file, ymmv depending on where you launch from
    :return: list where each page is a string
    """
    codec = 'utf-8'
    fp = file(path, 'rb')
    max_pgs = 0
    page_nos = set()

    text_pages = []
    for page in PDFPage.get_pages(fp, page_nos, maxpages=max_pgs, password='', caching=True, check_extractable=True):
        manager = PDFResourceManager()
        page_channel = StringIO()
        layout = LAParams()
        device = TextConverter(manager, page_channel, codec=codec, laparams=layout)
        interpreter = PDFPageInterpreter(manager, device)
        interpreter.process_page(page)
        text_pages.append(page_channel.getvalue())
    return text_pages


def convert_all_pdf_to_txt(path):
    """
    Returns all text in PDF as one long string
    :param path: string path to your file, ymmv depending on where you launch from
    :return: full contents
    """
    manager = PDFResourceManager()
    text_out = StringIO()
    codec = 'utf-8'
    layout = LAParams()
    device = TextConverter(manager, text_out, codec=codec, laparams=layout)
    fp = file(path, 'rb')
    interpreter = PDFPageInterpreter(manager, device)
    max_pgs = 0
    page_nos = set()

    for page in PDFPage.get_pages(fp, page_nos, maxpages=max_pgs, password='', caching=True, check_extractable=True):
        interpreter.process_page(page)

    text = text_out.getvalue()

    fp.close()
    device.close()
    text_out.close()
    return text