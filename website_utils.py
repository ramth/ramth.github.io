

def escape_for_html(raw_code,escaped_code):

	with open(raw_code) as input, open(escaped_code,'w+') as out:
		for line in input:
			line = line.rstrip()
		
			escape_list = (("&","&amp"),
						("<","&lt"),
						(">","&gt"))

			for old,new in escape_list:
				line = line.replace(old,new)
			
			out.write(line+'\n')
		
		
if __name__ == "__main__":
	escape_for_html('wix_code.txt','wix_escaped_code.txt')
		