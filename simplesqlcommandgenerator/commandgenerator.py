

class CommandGenerator:
    @classmethod
    def create_insert_command(cls, table_name: str, insert_items: dict) -> str:
        '''
        Example:
        insert_items = {
            "item": "hat",
            "quantity": 9,
            "price": 9,
        }

        :param table_name:
        :param insert_items:
        :return:
        '''
        key_list, value_list = cls.__create_key_value_str_from_object(obj=insert_items, join_str=", ")
        command = "INSERT INTO {} ({}) VALUES ({});".format(table_name, key_list, value_list)
        return command

    @classmethod
    def create_update_command(cls, table_name: str, set_items: dict, where_items: dict) -> str:
        '''
        Example:
        set_items = {
            "quantity": 25,
            "price": 4.5,
        }

        where_items = {
            "item": 'glove'
        }

        :param table_name:
        :param set_items:
        :param where_items:
        :return:
        '''
        set_items_str = cls.__create_str_from_object(obj=set_items, join_str=", ")
        where_items_str = cls.__create_str_from_object(obj=where_items, join_str="AND ")
        command = "UPDATE {} SET {} WHERE {};".format(table_name, set_items_str, where_items_str)
        return command

    @classmethod
    def create_delete_command(cls, table_name: str, where_items: dict) -> str:
        '''
        Example:
        where_items = {
            "item": 'glove'
        }

        :param table_name:
        :param where_items:
        :return:
        '''

        where_items_str = cls.__create_str_from_object(obj=where_items, join_str="AND ")
        command = "DELETE FROM {} WHERE {};".format(table_name, where_items_str)
        return command


    @classmethod
    def create_table_command(cls, table_name: str, table_cols: list) -> str:
        '''
        Example:
        table_cols = [
            ['item', 'VARCHAR(255)' , 'NOT NULL UNIQUE'],
            ['quantity', 'INT', 'NOT NULL'],
            ['price', 'DECIMAL(3,2)', 'NOT NULL'],
        ]
        :param table_name:
        :param table_cols:
        :return:
        '''
        command = "CREATE TABLE {} (".format(table_name)

        for ind, table_col in enumerate(table_cols):
            column_name = table_col[0]
            column_type = table_col[1]
            command += "{} {}".format(column_name, column_type)

            if len(table_col) > 2:
                column_constraint = table_col[2]
                command = "{} {}".format(command, column_constraint)

            if ind < len(table_cols) - 1:
                command += ","
        command += ");"

        return command



    # Utility Methods
    @classmethod
    def __create_str_from_object(cls, obj: dict, join_str: str):
        set_list = []
        for k, v in obj.items():
            if isinstance(v, str):
                set_list.append("{}='{}'".format(k, v))
            else:
                set_list.append("{}={}".format(k, v))

        return join_str.join(set_list)

    @classmethod
    def __create_key_value_str_from_object(cls, obj: dict, join_str: str):
        key_arr = []
        value_arr = []

        for k, v in obj.items():
            key_arr.append(k)

            if isinstance(v, str):
                value_arr.append("'{}'".format(v))
            else:
                value_arr.append("{}".format(v))

        return join_str.join(key_arr), join_str.join(value_arr)



