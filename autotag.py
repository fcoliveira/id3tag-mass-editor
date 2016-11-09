import eyeD3, os, re

num_errors = 0
successful_updates = 0

for root, dirs, files in os.walk(".", topdown = False):
	
	path_list = re.split("/", root)
	try:
		#autotag script should be in root folder
		artist_name = path_list[1]
		album_name = path_list[2]
	except:
		pass
		
	for file_name in files:
		if file_name.endswith(".mp3"):
			path = root + "/" + file_name # <- nao tem outro jeito?
			#obtem string do endereco completo do arquivo .mp3
			print(path)
				
			try:		
				
				track_name = re.split("\.", file_name) # <- definir um metodo especifico pra isso?
				#used only for updating the track name tag
				
				mp3_file = eyeD3.Tag() 
				mp3_file.link(path) # links file located in 'path'
				
				print("Tag version: %d.%d" %(mp3_file.getMajorVer(), mp3_file.getMinorVer())) #new methods added to file tag.py, line 1013
				if(mp3_file.getMajorVer() != 2 or (mp3_file.getMajorVer() == 2 and mp3_file.getMinorVer() != 4)):
					mp3_file.setVersion(eyeD3.ID3_V2_4)
					print("Tag updated to v2.4!")
				#mp3_file.setTextEncoding(eyeD3.UTF_16_ENCODING)
				# set of possible encodings:
				#mp3_file.setTextEncoding(eyeD3.UTF_8_ENCODING)
				#mp3_file.setTextEncoding(eyeD3.LATIN1_ENCODING)
				
				print("--- Old tag:")
				print("\tArtist: " + mp3_file.getArtist())
				print("\tAlbum: " + mp3_file.getAlbum() + "\n")		
				
				mp3_file.setArtist(artist_name)
				mp3_file.setAlbum(album_name)		
				mp3_file.update() #<- commits changes to file
				
				print("--- New tag:")
				print("\tArtist: " + mp3_file.getArtist())
				print("\tAlbum: " + mp3_file.getAlbum() + "\n") 
				
				successful_updates += 1			
					
			except:
				print("Error processing file!\n")
				num_errors += 1

print("End of processing!")
print("Updated files: %d" %successful_updates)
print("Files not updated: %d" %num_errors)
