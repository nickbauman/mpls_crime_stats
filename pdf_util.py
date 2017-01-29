from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO


def convert_pdf_to_txt_as_pages(path, limit=None):
    """
    returns a list, in order, of all pages start to finish
    :param path: string path to your file, ymmv depending on where you launch from
    :return: list where each page is a string
    """
    codec = 'utf-8'
    max_pgs = 0
    page_nos = set()
    text_pages = []
    index = 0
    with open(path, 'rb') as fd:
        for pg in PDFPage.get_pages(fd, page_nos, maxpages=max_pgs, password='', caching=True, check_extractable=True):
            manager = PDFResourceManager()
            page_channel = StringIO()
            layout = LAParams()
            device = TextConverter(manager, page_channel, codec=codec, laparams=layout)
            interpreter = PDFPageInterpreter(manager, device)
            interpreter.process_page(pg)
            text_pages.append(page_channel.getvalue())
            index += 1
            if limit and limit == index:
                break

    return text_pages


def convert_all_pdf_to_txt(path):
    """
    Returns all text in PDF as one long string
    :param path: string path to your file, ymmv depending on where you launch from
    :return: full contents
    """
    manager = PDFResourceManager()
    text_out = StringIO()
    layout = LAParams()
    device = TextConverter(manager, text_out, codec='utf-8', laparams=layout)
    interpreter = PDFPageInterpreter(manager, device)
    max_pgs = 0
    page_nos = set()

    with open(path, 'rb') as fd:
        for pg in PDFPage.get_pages(fd, page_nos, maxpages=max_pgs, password='', caching=True, check_extractable=True):
            interpreter.process_page(pg)
        text = text_out.getvalue()
        text_out.close()
        device.close()

    return text
