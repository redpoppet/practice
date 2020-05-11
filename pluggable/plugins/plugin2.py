def sayGoodbye(self,from_):
    print("good bye from %s. " % from_)

class plugin2:
    def setPlatform(self,platform):
        self.platform=platform
        if platform is not None:
            platform.__class__.sayGoodbye=sayGoodbye

    def stop(self):
        self.platform.sayGoodbye("plugin2")

    def start(self):
        self.platform.sayHello("plugin2")



def getPluginClass():
    return plugin2
