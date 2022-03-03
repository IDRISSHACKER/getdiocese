class Month:
    def __init__(self):
        super(Month, self).__init__()
        self.months = {
            1: "Janvier",
            2: "Fevrier",
            3: "Mars",
            4: "Avril",
            5: "Mai",
            6: "Juin",
            7: "Juillet",
            8: "Août",
            9: "Septembre",
            10: "Octobre",
            11: "Novembre",
            12: "Decembre"
        }

    def getMonths(self):
        return self.month;

    def getMonthsTab(self):
        tabMonth = [ ]

        for index in self.months:
            tabMonth.append(self.months.get(index))

        return tabMonth


if __name__ == "__main__":
    anne = Month()

    print(anne.getMonthsTab())
