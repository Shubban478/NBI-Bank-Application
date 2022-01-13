class DataSource:
    # host
    def datasource_conn(self):
        pass  # Denna metod implementerar kopplingen till en generisk datasource. Returnerar
        # en <class ‘tuple’> med en <class ‘bool’> och en <class ‘str’> t.ex., (True,
        # “Connection successful” [, datasource namn])

    def get_all(self):
        pass  # Returnerar alla kunder i banken.

    def update_by_id(self, id):
        pass  # Uppdaterar en kund baserad på id:n som angetts som parameter. Returnerar
        # info om kunden som uppdaterats, eller -1 om kunden inte finns.

    def find_by_id(self, id):
        pass  # Returnerar en kund baserad på id:n som angetts eller -1 om kunden in finns.

    def remove_by_id(self, id):
        pass  # Raderar en kund baserad på id:n som angetts som parameter. Returnerar info
        # om kunden som tagits bort eller -1 om kunden inte finns.
