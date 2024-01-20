import keyboard, sys, pickle, os, csv, time, pystray, ctypes
from collections import defaultdict
from PIL import Image
import threading

bin_path = "./output/key_presses.pkl"
csv_path = "./output/output.csv"
global key_presses
key_presses = defaultdict(int)
auto_save_interval:float = 600

if os.path.exists(bin_path):
  print("Loading existing file...")
  with open(bin_path, 'rb') as f:
      key_presses = pickle.load(f)
      print(key_presses)
else:
  print("No existing file found, dictionary will be saved to new file.")

def is_admin():
  try:
    return ctypes.windll.shell32.IsUserAnAdmin()
  except:
     return False

if is_admin():
  def save_bin():
    global key_presses
    with open(bin_path, 'wb') as f:
      pickle.dump(key_presses, f)
      print("Saved dictionary to binary file!")

  def save_csv():
    global key_presses
    with open(csv_path, 'w', newline='') as output_file:
      keys = key_presses.keys()
      dict_writer = csv.writer(output_file)
      dict_writer.writerow(list(keys))
      dict_writer.writerow([str(value) for value in key_presses.values()])
      print("Saved dictionary to csv file!")

  def exit():
    print("Received exit command, saving files and closing script!")
    save_bin()
    save_csv()
    os._exit(0)

  def autosaver():
    try:
      while True:
        print("Performing autosave...")
        save_bin()
        save_csv()
        time.sleep(auto_save_interval)
    except KeyboardInterrupt:
      exit()

  def create_image():
    image = Image.open("icon.png")
    return image
  def close_icon(icon):
    icon.stop()
    exit()

  def run_icon():
    image = create_image()
    icon = pystray.Icon("name", image, "Pycat is counting your keystrokes!", menu=pystray.Menu(
      pystray.MenuItem("Exit", close_icon)
    ))
    icon.run()

  def key_loop():
    try:
      def on_key_event(event):
        global key_presses
        key_presses[event.name] += 1
        print(key_presses)
      keyboard.hook(on_key_event)

      while True:
        time.sleep(0.45)

    except KeyboardInterrupt:
      exit()
      
  if __name__ == '__main__':
    t1 = threading.Thread(target=run_icon)
    t2 = threading.Thread(target=key_loop)
    t3 = threading.Thread(target=autosaver)
    
    t1.start()
    t2.start()
    t3.start()
    
    t1.join()
    t2.join()
    t3.join()
else:
  ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)