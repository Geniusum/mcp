import os
import shutil

class MCP():
    def __init__(self) -> None:
        self.script_path = os.path.dirname(os.path.abspath(__file__))
        self.temp_path = os.path.join(self.script_path, "temp")
        self.out_path = os.path.join(self.script_path, "out")
        self.ExistsDirOrMake(self.temp_path)
        self.ExistsDirOrMake(self.out_path)

    def ExistsDirOrMake(self, path):
        if not os.path.exists(self.temp_path): os.mkdir(path)

    def SecureCompressProcess(self, path:str, output:str=None):
        data = []
        name = os.path.splitext(path)[0]
        if not output:
            output = self.out_path
        msc = os.path.join(output, name + ".msc")
        if os.path.exists(msc):
                os.remove(msc)
        if not os.path.exists(path):
            exit("This path don't exists.")
        if os.path.isfile(path):
            if os.path.exists(os.path.join(self.temp_path, name)):
                os.remove(os.path.join(self.temp_path, name))
            os.mkdir(os.path.join(self.temp_path, name))
            shutil.copyfile(path, os.path.join(self.temp_path, name))
            path = os.path.join(self.temp_path, name)
        for root, dirs, files in os.walk(path):
            for file in files:
                file_path = os.path.join(root, file)
                data.append([file_path, open(os.path.abspath(file_path)).read()])
            for dir in dirs:
                dir_path = os.path.join(root, dir)
                data.append([dir_path])
        print(data)