import re, glob



START_PATH = "."
tree = {}

def main(path):
	tmp_tree = {}

	def search(path):
		print(f"->searching modules in {path} …")
		module_list = glob.glob(path+"\\*.py")
		if not module_list:
			print("->no modules found in this directory")
			return None
		print(f"->found module(s):\n->\n->{'\n->'.join(module_list)}\n->")
		return module_list

	def analyze(module_list):
		for module in module_list:
			print(f"->analyzing module '{module}' …")
			with open(module) as mdl:
				mdl_text = mdl.read()
			reqs = re.findall(r"^\s+import\s+([\w\-]+,?\s?)+", mdl_text)
			# reqs might:[("mdl_name0, ","mdl_name1, ",…")]
			if not reqs:
				tmp_tree[module] = " "
				continue
			reqs = map(lambda req:re.sub(r",\s","",req[0])+".py",reqs)
			# reqs might:["mdl_name0.py","mdl_name1.py",…]



if __name__ == "__main__":
	path = input("?target directory> ")
	main(path)