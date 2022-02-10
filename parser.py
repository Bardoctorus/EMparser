import sys


filepath = 'input/ems072.txt' 

if len(sys.argv) > 1:
    epno = int(sys.argv[1])
    yturl = str(sys.argv[2])
    intro = str(sys.argv[3])
else:
    sys.exit("usage: python3 parser.py EPISODENUMBER YOUTUBEURL")
print(epno)

#make file for youtube
ytf = open("output/youtubedesc.txt", 'a')
#make file for libsyn
lsf = open("output/libsyndesc.txt" , 'a')
#make file for mailchimp
mcf = open("output/mailchimplist" , 'a')


# function for youtube
def makeYT(lines):
    counter = 1
    while(counter < len(lines)-1):
        text = lines[counter-1]
        link = lines[counter]

        ytf.write(text.strip('\n')+ ': '+link)
        counter+=3

    ytf.write("----------------------------------------------------------i\n")
    counter = 1
    while(counter < len(lines)-1):
        text = str(lines[counter-1]).strip('\n')
        number = lines [counter+1]
        ytf.write(text+' '+number)
        counter+=3

# function for libsyn
def makeLS(lines):
    pre = ('<p>This week\'s Electromaker Show is now available on YouTube and everywhere you get your podcasts!</p>\
<p><span style="font-weight: 400;">Welcome to the Electromaker Show episode {}! {}</span></p>\
<p>Tune in for the latest maker, tech, DIY, IoT, embedded, and crowdfunding news stories from the week.</p>\
<p>&nbsp;</p>\
<p><iframe title="YouTube video player" src="https://www.youtube.com/embed/{}" width="560" height="315" frameborder="0"></iframe></p>\
<p><span style="font-weight: 400;"><a href="https://www.youtube.com/watch?v={}">Watch the show!</a></span></p>\
<p><span style="font-weight: 400;">We publish a new show every week. Subscribe here:</span> <a href="https://www.youtube.com/channel/UCiMO2NHYWNiVTzyGsPYn4DA?sub_confirmation=1"> <span style="font-weight: 400;">https://www.youtube.com/channel/UCiMO2NHYWNiVTzyGsPYn4DA?sub_confirmation=1</span></a></p>\
<p><span style="font-weight: 400;">We stock the latest products from Adafruit, Seeed Studio, Pimoroni, Sparkfun, and many more! Browse our shop:</span></p>\
<p><a href="https://www.youtube.com/redirect?event=video_description&amp;redir_token=QUFFLUhqbVI1SkM3TXE2Z3g4MzhqUHRUTFVkZVlBSEx0QXxBQ3Jtc0trOFhxMS1kLXdtQWNrYzFwMlhRN05Jako3WVgteVB3YWQ1MXg0YjNQVXdRRDJJeHNxVmZnTmF4cnpjYlZXQzRkUW9SRXN6cFVDTDBtR2pjLXVrYmtLR3EyekFvOC1INnE0Uk1OdDJTSXBmbXBqNTdkcw&amp;q=https%3A%2F%2Fwww.electromaker.io%2Fshop"> <span style="font-weight: 400;">https://www.electromaker.io/shop</span></a></p>\
<p><span style="font-weight: 400;">Join us on Discord!</span> <a href="https://discord.com/invite/w8d7mkCkxj%E2%80%8B"><span style="font-weight: 400;">https://discord.com/invite/w8d7mkCkxj​</span></a></p>\
<p><span style="font-weight: 400;">Follow us on Twitter:</span> <a href="https://twitter.com/ElectromakerIO"><span style="font-weight: 400;">https://twitter.com/ElectromakerIO</span></a></p>\
<p><span style="font-weight: 400;">Like us on Facebook:</span> <a href="https://www.facebook.com/electromaker.io/"><span style="font-weight: 400;">https://www.facebook.com/electromaker.io/</span></a></p>\
<p><span style="font-weight: 400;">Follow us on Instagram:</span> <a href="https://www.instagram.com/electromaker_io/"><span style="font-weight: 400;">https://www.instagram.com/electromaker_io/</span></a></p>\
<p>Featured in this show:</p>\
<ul>'.format(str(epno),str(intro), str(yturl),str(yturl)))
    lsf.write(pre)
    counter = 1
    while(counter < len(lines)-1):
        text = lines[counter-1]
        link = lines[counter]

        lsf.write('<li><a href="'+str(link)+'">'+str(text)+'</a></li>'+'\n')
        counter+=3
    

    lsf.write('</ul>')


# function for mailchimp
def makeMC(lines, epno, yturl):
    #prepend file with boilerplate
    prepend = ('<h3><span style="color:#000000">Electromaker Show Episode '+ str(epno)+ ' Highlights:</span></h3><ul>')
    mcf.write(prepend)
    
    counter = 1
    for line in lines:
        if counter % 3 == 0:
            #parse mins:seconds into int inseconds for url
            print('ifmod3: {}'.format(line))
            x, y = str(line).split(':')
            mins = int(x)
            secs = int(y)
            inseconds = (mins*60)+secs

            link = '<li><a href="https://www.youtube.com/watch?v={}&amp;t={}s" target="_blank">{}</a></li>'.format(yturl,inseconds,text)
            mcf.write(link)
        else:
            if 'https://' in line:
                
                print('if https: {}'.format(line))
                pass
            else:
                print('if else else: {}'.format(line))
                text = str(line)
    #increment the counter stoopod
        counter+=1

    #add the closing unordered list tag
    mcf.write('</ul>')
# open the input file
with open(filepath, 'r') as f:
    #get lines and start counter
    print('fileopen')
    lines = f.readlines()
    counter = 0
    print('line1: {}, line2: {}'.format(lines[0].strip('\n'),lines[1]).strip('\n'))
    # send each line to a different text maker thing
    makeYT(lines)
    makeLS(lines)
    makeMC(lines,epno,yturl)


ytf.close()
lsf.close()
mcf.close()
