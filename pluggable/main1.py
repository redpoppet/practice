import os
import importlib
import zipfile
import  configparser 
import sys

class Platform:
    def __init__(self):
        self.plugins=[]
        self.loadPlugins()
    
    def sayHello(self,from_):
        print('hello from %s.' % from_)
    
    def loadPlugins(self):
        for filename in os.listdir("./plugins"):
            if not filename.endswith(".zip"):
                continue
            self.runPlugin(filename)


    def runPlugin(self,filename):
        pluginPath=os.path.join("plugins",filename)
        pluginInfo,plugin = self.getPlugin(pluginPath)
        # print(pluginInfo)
        print("loading plugin:%s, description: %s " % (pluginInfo["name"],pluginInfo['description']) )
        plugin.setPlatform(self)
        plugin.start()

    def getPlugin(self,pluginPath):
        pluginzip = zipfile.ZipFile(pluginPath,"r")
        description_txt=pluginzip.open("description.txt").read().decode('ascii')
        parser=configparser.ConfigParser()
        parser.read_string(description_txt)

        pluginInfo={}

        pluginInfo["name"]=parser.get('general','name')
        pluginInfo["description"]=parser.get("general","description")
        pluginInfo["code"]=parser.get("general","code")
        print(pluginInfo)
        sys.path.append(pluginPath)
        moduleName,pluginClassName=pluginInfo["code"].rsplit(".",1)
        print(moduleName,pluginClassName)
        module = __import__(moduleName,fromlist=[pluginClassName,])
        pluginClass=getattr(module,pluginClassName)
        plugin=pluginClass()
        return pluginInfo,plugin


    def shutdown(self):
        for o in self.plugins:
            o.stop()
            o.setPlatform(None)
        self.plugins=[]

 
if __name__ == "__main__":
    platform=Platform()
    platform.shutdown()

        
