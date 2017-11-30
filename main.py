from ConfigurationManager.ConfigurationManager import Configuration
from CompareService.CompareService import CompareService


def main():
    Configuration.get_configuration()
    compare_service = CompareService()
    compare_service.compare()

if __name__ == "__main__":
    main()