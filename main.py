from PIL import Image
import os
import time
import datetime
import threading



# Optimize function
def optimize(num):
 mylistfile = open("thread-"+str(num)+".txt", "r")
 for filename in mylistfile:
  filename = filename.replace('\n', "")
  im = Image.open("stare/"+filename)
  im.thumbnail((1000, 1000))
  im.save("nowe/"+filename,optimize=True,quality=45)
 mylistfile.close()
 return num;

# Comment time End
def log(message):
 now = datetime.datetime.now().strftime("%H:%M:%S")
 print("\n")
 print "%s %s" % (now, message)
 print("\n")

# Threading 
class ThreadGoing(threading.Thread):
 def __init__(self, value):
  threading.Thread.__init__(self)
  self.value = value
 def run(self):
  print(self.value)
  result = optimize(self.value)
  log("%s -> %s ||| This thread finish " % (self.value, result))

# Partition to lists
def partitionList(manyThread):
 i = 0
 f = os.listdir("stare")
 for line in f:
  i += 1
 allItems = i
 print(allItems)
 thread = allItems / manyThread
 y = 0 
 while y < manyThread -1 :
  print(thread)
  y += 1

 threadLast = (allItems / manyThread) + (allItems%manyThread)
 print(threadLast)
 
 if(allItems != thread * (manyThread - 1) + threadLast ):
  print("Error checksum !!!")
 else:
  print("===================")
  print(" Checksum Good :)")
  print("===================")
  time.sleep(2.4)

 j = 0
 x = 1 # TMP thread
 f2 = os.listdir("stare")
 for singleLine in f2:
  if(x <= manyThread-1):
   if(j < thread):
    fth = open("thread-"+str(x)+".txt", "a")
    fth.write(singleLine)
    fth.write("\n")
    fth.close()
    j += 1
   else:
    j = 0
    x += 1
  else: 
   if(j < threadLast):
    fth = open("thread-"+str(x)+".txt", "a")
    fth.write(singleLine)
    fth.write("\n")
    fth.close()

def main():
 print("How many threads do you want to use?\n")
 theads = input()
 if(theads >= 17):
  return 0
 print("Quality images(1-100):\n")
 quality = input()
 if(quality > 100):
  return 0
 if(quality < 0):
  return 0
 partitionList(theads)
 log("Start main Thread")
 i = 1
 while i <= theads :
  ThreadGoing(i).start()
  i += 1
 log("End main Thread")
 j = 1
 time.sleep(2.4)
 while j <= theads :
  os.remove("thread-"+str(j)+".txt")
  j += 1 
 
if __name__ == "__main__":
 main()
