class Configuration:
    dir_path = ""
    spread_name = ""

    @staticmethod
    def set_configuration():
        config_file = ("config.txt", "r")

        with open('config.txt') as fin:
            for line in fin:
                setting, value = line.split("=")
                value = value.replace("\"", "")
                if setting == "dir_path":
                    Configuration.dir_path = value
                elif setting == "spread_name":
                    Configuration.spread_name = value

        print(Configuration.spread_name)
        print(Configuration.dir_path)


