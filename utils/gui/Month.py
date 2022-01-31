class Month:
    def __init__(self, select):
        super(Month, self).__init__()
        self.select = select
        months = {0: "Janvier", 1: "Fevrie", 2: "Mars", 3: "Avril", 4: "Mai", 5: "Juin", 6: "Juillet", 7: "Août", 8: "Septembre", 9:"Octobre", 10:"Novembre", 11:"Decembre"}
        self.months = {
            0: "Janvier",
            1: "Fevrie",
            2: "Mars",
            3: "Avril",
            4: "Mai",
            5: "Juin",
            6: "Juillet",
            7: "Août",
            8: "Septembre",
            9:"Octobre",
            10:"Novembre",
            11:"Decembre"
        }

    def getMonths(self):
        return self.month;

    def getMonthsTab(self):
        tabMonth = []

        for index in self.months:
            tabMonth[index] = self.months.get(index)

        return tabMonth

    def setMonthInSelect(self):
        for index in self.months:
            self.select.addItem(self.months.get(index), index)


anne = Month("m")

print(anne.getMonthsTab())