class DocumentPrinting:

    state = 0

    def print(self):
        if self.state == 2:
            # print document, if okay then
            self.state = 0
            pass

    def check_toner(self):
        # check toner
        self.state += 1

    def check_paper(self):
        # check paper, if okay then
        self.state += 1

def doc_printing_test():
    # set
    printing = DocumentPrinting()

    # act
    printing.check_paper()
    printing.check_toner()
    printing.print()

    # asser
    if printing.state != 0:
        # the test is failed
        pass
