import shutil
original = r'D:\\JenkinsHome\\workspace\\PipelineOne\\Hello.py'
target = r'D:\\JenkinsHome\\workspace\\PipelineOne\\[REALEASE]\\Hello.exe'
shutil.move(original,target)
shutil.make_archive("Hello.exe","zip", root_dir)
