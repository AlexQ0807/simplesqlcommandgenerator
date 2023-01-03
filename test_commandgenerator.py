from unittest import TestCase

from simplesqlcommandgenerator.commandgenerator import CommandGenerator


class TestCommandGenerator(TestCase):
    def test_create_insert_command(self):
        table_name = "Customers"
        insert_items = {
            "CustomerName": "Cardinal",
            "ContactName": "Tom B. Erichsen",
            "Address": "Skagen 21",
            "City": "Stavanger",
            "PostalCode": "4006",
            "Country": "Norway",
        }
        cmd = CommandGenerator.create_insert_command(table_name=table_name, insert_items=insert_items)
        expected = "INSERT INTO Customers (CustomerName, ContactName, Address, City, PostalCode, Country) " \
                   "VALUES ('Cardinal', 'Tom B. Erichsen', 'Skagen 21', 'Stavanger', '4006', 'Norway');"

        print(cmd)
        print(expected)
        self.assertEqual(cmd.replace(" ", "").replace("\t", "").replace("\n", ""),
                         expected.replace(" ", "").replace("\t", "").replace("\n", ""))

    def test_create_update_command(self):
        table_name = "Customers"
        set_items = {
            "ContactName": "Alfred's Schmidt",
            "City": "Frankfurt",
        }

        where_items = {
            "CustomerID": 1
        }

        cmd = CommandGenerator.create_update_command(table_name=table_name,
                                                     set_items=set_items,
                                                     where_items=where_items)

        expected = "UPDATE Customers SET ContactName = 'Alfred\\'s Schmidt', City= 'Frankfurt' WHERE CustomerID = 1;"

        print(cmd)
        print(expected)

        self.assertEqual(cmd.replace(" ", "").replace("\t", "").replace("\n", ""),
                         expected.replace(" ", "").replace("\t", "").replace("\n", ""))

    def test_create_delete_command(self):
        table_name = "Customers"
        where_items = {
            "CustomerName": 'Alfreds Futterkiste'
        }

        cmd = CommandGenerator.create_delete_command(table_name=table_name,
                                                     where_items=where_items)
        expected = "DELETE FROM Customers WHERE CustomerName='Alfreds Futterkiste';"

        print(cmd)
        print(expected)

        self.assertEqual(cmd.replace(" ", "").replace("\t", "").replace("\n", ""),
                         expected.replace(" ", "").replace("\t", "").replace("\n", ""))

    def test_create_table_command(self):
        table_name = "Persons"
        table_cols = [
            ['PersonID', 'int', 'NOT NULL PRIMARY KEY'],
            ['LastName', 'varchar(255)', 'NOT NULL'],
            ['FirstName', 'varchar(255)', 'NOT NULL'],
            ['Address', 'varchar(255)'],
            ['City', 'varchar(255)'],
        ]

        cmd = CommandGenerator.create_table_command(table_name=table_name,
                                                    table_cols=table_cols)
        expected = '''
            CREATE TABLE Persons (
                PersonID int NOT NULL PRIMARY KEY,
                LastName varchar(255) NOT NULL,
                FirstName varchar(255) NOT NULL,
                Address varchar(255),
                City varchar(255)
            );
        '''

        print(cmd.replace(" ", "").replace("\t", "").replace("\n", ""))
        print(expected.replace(" ", "").replace("\t", "").replace("\n", ""))

        self.assertEqual(cmd.replace(" ", "").replace("\t", "").replace("\n", ""),
                         expected.replace(" ", "").replace("\t", "").replace("\n", ""))
