import subprocess, time
from settings import conf

class AllureHandler(object):

    def execute_command(self):
        time.sleep(1)
        subprocess.call(conf.ALLURE_COMMAND, shell=True)

if __name__ == "__main__":
    allu = AllureHandler()
    temp = allu.execute_command()
    print(temp)
