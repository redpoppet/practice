import os
import importlib
import zlibfile


class Platform:
    def __init__(self):
        self.plugins =[]
        self.loadPlugins()
    
    def sayHello(self,from_):
        print('hello from %s.' % from_)
    
    def loadPlugins(self):
        for filename in os.listdir("./plugins"):
            if not filename.endswith(".py") or filename.startswith("_"):
                continue
            self.runPlugin(filename)

    def runPlugin(self, filename):
        pluginName=os.path.splitext(filename)[0]
        plugin=importlib.import_module("plugins."+pluginName)
        clazz = plugin.getPluginClass()
        o=clazz()
        o.setPlatform(self)
        o.start()
        self.plugins.append(o)

    def shutdown(self):
        for o in self.plugins:
            o.stop()
            o.setPlatform(None)
        self.plugins=[]


if __name__ == "__main__":
    platform=Platform()
    platform.shutdown()

        
