import os
import sys

class FileExplorerCLI:
	def __init__(self):
		self.current_path = os.getcwd()
	
	def list_dirs(self): #ls 
		try:
			items = os.listdir(self.current_path)
			for item in items:
				print(item)
		except Exception as e:
			print(f"Error listing the directory: {e}")
	
	def change_directory(self, path): #cd
		try:
			new_path = os.path.abspath(os.path.join(self.current_path, path))
			if os.path.isdir(new_path):
				self.current_path = new_path
				os.chdir(self.current_path)
				print(f"Changed directory to {self.current_path}")
			else:
				print("Directory not found!")
		except Exception as e:
			print(f"Error changing directory: {e}")

	def delete_file(self, file_name): #rm 
		try:
			file_path = os.path.join(self.current_path, file_name)
			if os.path.isfile(file_path):
				os.remove(file_path)
				print(f"Deleted {file_name}")
			else:
				print("Fill not found!")
		except Exception as e:
			print(f"Error deleting {file_name}: {e}")
	
	def rename_file(self, old_name, new_name): #mv 
		try:
			old_path = os.path.join(self.current_path, old_name)
			new_path = os.path.join(self.current_path, new_name)
			if os.path.exists(old_path):
				os.rename(old_path, new_path)
				print(f"Renamed {old_name} to {new_name}")
			else:
				print(f"{old_name} is not found")
		except Exception as e:
			print(f"Error renaming {old_name}: {e}")
	
	def main(self):
		while True:
			print(f"\n\nCurrent Directory: {self.current_path}")
			command = input("Enter command (ls, cd <dir>, rm <file>, mv <old_name> <new_name>, exit): ").strip().split()
			
			if not command:
				continue
			
			cmd = command[0] 
			
			if cmd == "ls":
				if len(command) == 1:
					self.list_dirs()
				else:
					print("Wrong usage. Hint: ls ")
			elif cmd == "cd":
				if len(command) ==2:
					self.change_directory(command[1])
				else:
					print("Wrong usage. Hint: cd <directory> (for nested directories: cd <dic1/dic2>)")
			elif cmd == "rm":
				if len(command)>1:
					for file_name in command[1:]:
						self.delete_file(file_name)
				else:
					print("Wrong usage. Hint: rm <file>")
			elif cmd == "mv":
				if len(command)==3:
					self.rename_file(command[1], command[2])
				else:
					print("Wrong usage. Hint: mv <old_name> <new_name>")
			elif cmd == "exit":
					if len(command) == 1:
						print("Exiting")
						sys.exit(0)
					else:
						print("Wrong usage. Hint: exit ")
			else:
				print("Unknown command. Try again!")

if __name__ =="__main__":
	explorer = FileExplorerCLI()
	explorer.main()





			
	
