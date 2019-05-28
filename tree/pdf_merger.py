from PyPDF2 import PdfFileMerger
from PyPDF2.generic import NumberObject, NameObject


class PdfMerger(PdfFileMerger):

    def _trim_outline(self, pdf, outline, pages):
        """
        Removes any outline/bookmark entries that are not a part of the
        specified page set.
        """
        new_outline = []
        prev_header_added = True
        for i, o in enumerate(outline):
            if isinstance(o, list):
                sub = self._trim_outline(pdf, o, pages)
                if sub:
                    if not prev_header_added:
                        new_outline.append(outline[i - 1])
                    new_outline.append(sub)
            else:
                prev_header_added = False
                for j in range(*pages):
                    is_equal = False
                    page = None
                    page_object = o['/Page'].getObject()
                    if isinstance(page_object, NumberObject):
                        is_equal = pdf.getPageNumber(pdf.getPage(j)) == page_object.as_numeric()
                        page = NumberObject(page_object.as_numeric() + self.id_count)
                    else:
                        is_equal = pdf.getPage(j).getObject() == o['/Page'].getObject()
                        page = o[NameObject('/Page')] = o['/Page'].getObject()
                    if is_equal:
                        o[NameObject('/Page')] = page
                        new_outline.append(o)
                        prev_header_added = True
                        break
        return new_outline
