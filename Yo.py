import shutil
original = r'D:\\JenkinsHome\\workspace\\PipelineOne\\Hello.py'
target = r'D:\\JenkinsHome\\workspace\\PipelineOne\\Hello.exe'
shutil.move(original,target)

o = r'D:\\JenkinsHome\\workspace\\PipelineOne\\Hello.exe'
t = r'D:\\JenkinsHome\\workspace\\PipelineOne\\[Release]\\Hello.zip'
shutil.move(o,t)
