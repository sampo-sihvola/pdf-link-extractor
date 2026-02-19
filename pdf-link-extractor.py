from pypdf import PdfReader

# change "file" to actual file name
reader = PdfReader('file.pdf')

link = "/Link"
a = "/A"
uri = "/URI"
link_list = []

for page in reader.pages:
	if "/Annots" in page:
		for annotation in page["/Annots"]:
			annotation_object = annotation.get_object()
			subtype = annotation_object["/Subtype"]
			if subtype == link:
				if a in annotation_object:
					link_list.append(annotation_object[a][uri])
	
# remove duplicate links
sorted_link_list = list(set(link_list))

with open ("links.txt", "w") as output:
	for link in sorted_link_list:
		output.write(link + "\n")
