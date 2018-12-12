import pygame,random,sys,glob,time

baixo = pygame.image.load("imgs/naipes/nbaixo.jpeg")
cima = pygame.image.load("imgs/naipes/ncima.jpg")

def spritess(sprites):
	display.blit(pygame.image.load(sprites1[0]), (0, 30))
	display.blit(pygame.image.load(sprites1[1]), (0, 150))
	display.blit(pygame.image.load(sprites1[2]), (0, 270))
	display.blit(pygame.image.load(sprites1[3]), (0, 400))
	display.blit(pygame.image.load(sprites2[0]), (103, 30))
	display.blit(pygame.image.load(sprites2[1]), (103, 150))
	display.blit(pygame.image.load(sprites2[2]), (103, 270))
	display.blit(pygame.image.load(sprites2[3]), (103, 400))
	display.blit(pygame.image.load(sprites3[0]), (206, 30))
	display.blit(pygame.image.load(sprites3[1]), (206, 150))
	display.blit(pygame.image.load(sprites3[2]), (206, 270))
	display.blit(pygame.image.load(sprites3[3]), (206, 400))
	display.blit(background,(0,30))
	display.blit(barra,(0,230))
	display.blit(baixo,(0,340))
	display.blit(cima,(0,0))
	display.blit(Stop,(10,560))
	display.blit(spin,(185,550))
	display.blit(Cred,(80,565))
	display.blit(change,(237,0))


def load_sprites(path):
	sprites = glob.glob(path)
	return sprites


def jequiti(spin_t, sprites1, sprites2, sprites3, display):
	last_update = time.time()
	frame_rate = 0.025
	tempo_de_giro = random.randrange(1, 4)
	tempo_de_giro2 = random.randrange(1, 4)
	tempo_de_giro3 = random.randrange(1, 4)

	tempo_max = max(tempo_de_giro, tempo_de_giro2)
	tempo_max = max(tempo_de_giro3, tempo_max)

	while(abs(spin_t - time.time()) < tempo_max):
		if(tempo_de_giro > abs(last_update - time.time()) > frame_rate):
			last_update = time.time()
			sprites1[0], sprites1[1], sprites1[2], sprites1[3] = sprites1[3], sprites1[0], sprites1[1], sprites1[2]
			spritess(sprites1)
			pygame.display.flip()

		if(tempo_de_giro2 > abs(last_update - time.time()) > frame_rate):
			last_update = time.time()
			sprites2[0], sprites2[1], sprites2[2], sprites2[3] = sprites2[3], sprites2[0], sprites2[1], sprites2[2]
			spritess(sprites2)
			pygame.display.flip()

		if(tempo_de_giro3 > abs(last_update - time.time()) > frame_rate):
			last_update = time.time()
			sprites3[0], sprites3[1], sprites3[2], sprites3[3] = sprites3[3], sprites3[0], sprites3[1], sprites3[2]
			spritess(sprites3)
			pygame.display.flip()


def xcreditos(cred, coloc, last_update):
	if(abs(last_update - time.time()) > 1):
		credit.play()
		cred += 50
		coloc = coloc + 1
		last_update = time.time()
	return cred, coloc, last_update


def mcreditos(cred):
	make_it_happend = time.time()
	text_fim = font.render("OBRIGADO POR JOGAR", True, text_color)
	display.blit(text_fim,(10,200))
	lucro = cred - coloc*50
	text_ganho = font.render("Voce fez: {} creditos".format(lucro),True, text_color)
	display.blit(text_ganho,(10,230))
	pygame.display.flip()
	cred = 0
	while(abs(make_it_happend - time.time()) < 2):
		continue
	return cred


def creditos(cred):
	text_cred = font.render("Creditos: {}".format(cred), True, text_color)
	display.blit(text_cred,(0,0))

def mudar(curr, limite):
	global baixo, cima

	sprites1, sprites2, sprites3 = 0, 0, 0
	_curr = curr
	if(_curr == 0):
		sprites1 = load_sprites("imgs/naipes/n*.png")
		sprites2 = load_sprites("imgs/naipes/n*.png")
		sprites3 = load_sprites("imgs/naipes/n*.png")
		baixo = pygame.image.load("imgs/naipes/nbaixo.jpeg")
		cima = pygame.image.load("imgs/naipes/ncima.jpg")

	elif(_curr == 1):
		sprites1 = load_sprites("imgs/jogos/s*.jpg")
		sprites2 = load_sprites("imgs/jogos/s*.jpg")
		sprites3 = load_sprites("imgs/jogos/s*.jpg")
		baixo = pygame.image.load("imgs/jogos/jbaixo.jpeg")
		cima = pygame.image.load("imgs/jogos/scima.jpeg")

	elif(_curr == 2):
		sprites1 = load_sprites("imgs/animes/a*.jpeg")
		sprites2 = load_sprites("imgs/animes/a*.jpeg")
		sprites3 = load_sprites("imgs/animes/a*.jpeg")
		baixo = pygame.image.load("imgs/animes/abaixo.jpg")
		cima = pygame.image.load("imgs/animes/acima.jpg")


	_curr += 1
	if(_curr >= 3):
		_curr = 0
	return sprites1, sprites2, sprites3, _curr

def secret():
	global baixo, cima
	
	sprites1 = load_sprites("imgs/bombapatch/p*.jpeg")
	sprites2 = load_sprites("imgs/bombapatch/p*.jpeg")
	sprites3 = load_sprites("imgs/bombapatch/p*.jpeg")
	baixo = pygame.image.load("imgs/bombapatch/baixo.jpeg")
	cima = pygame.image.load("imgs/bombapatch/cima.jpeg")
	return sprites1, sprites2, sprites3

pygame.init()

size = width, height = 310, 600
display = pygame.display.set_mode(size)
pygame.display.set_caption("Slot Machine")
credit = pygame.mixer.Sound("Sons/credit.wav")
win = pygame.mixer.Sound("Sons/win.wav")
beep = pygame.mixer.Sound("Sons/Beep.wav")
giro = pygame.mixer.Sound("Sons/giro.wav")
barra = pygame.image.load("imgs/sprites/barra.png")
barra.set_colorkey((174,255,245))
spin = pygame.image.load("imgs/sprites/Spin.png")
spin.set_colorkey((255,174,201))
Stop = pygame.image.load("imgs/sprites/Stop.png")
Stop.set_colorkey((255,174,201))
change = pygame.image.load("imgs/sprites/change.png")
Cred = pygame.image.load("imgs/sprites/Creditos.png")
Cred.set_colorkey((255,174,201))
background = pygame.image.load("imgs/sprites/background.png")
sprites1 = load_sprites("imgs/naipes/n*.png")
sprites2 = load_sprites("imgs/naipes/n*.png")
sprites3 = load_sprites("imgs/naipes/n*.png")

text_color = (0,255,150)
font = pygame.font.Font(None,32)
cred = 0
coloc = 0
curr = 0 

last_update = [time.time(), time.time(), time.time(),time.time(),time.time()]

while True:
	for event in pygame.event.get():
		if(event.type == pygame.QUIT):
			pygame.quit()
			sys.exit()
	
	display.fill((0,0,0,255))
	keys = pygame.key.get_pressed()	
	
	if (event.type == pygame.MOUSEBUTTONDOWN ):
		mx,my = pygame.mouse.get_pos()

		if mx > 22 and mx <82 and my >564:
			credm = mcreditos(cred)
			coloc = 0
			cred = 0

		elif mx > 84 and mx <188 and my >570:
			cred, coloc, last_update[2] = xcreditos(cred, coloc, last_update[2])

		elif mx > 194 and mx <287 and my >555:
			last_update[1] = time.time()
			if cred >= 50:
				giro.play()
				spin_t = time.time()
				jequiti(spin_t, sprites1, sprites2, sprites3, display)
				cred = cred - 50
				if sprites1[2] == sprites2[2] == sprites3[2]:
					win.play()
					cred = cred +550
					make_it_happend = time.time()
					text_ganharcred = font.render("Voce Ganhou 500 creditos!", True, text_color)
					display.blit(text_ganharcred,(0,310))
					pygame.display.flip()
					while(abs(make_it_happend - time.time()) < 2):
						continue

					display.blit(text_ganharcred,(0,550))

			if cred < 50:
				beep.play()
				make_it_happend = time.time()
				text_Semcred = font.render("Voce precisa colocar creditos", True, text_color)
				display.blit(text_Semcred,(0,310))
				pygame.display.flip()
				while(abs(make_it_happend - time.time()) < 1.5):
					continue

		elif (mx > 235 and my < 24 and abs(last_update[3] - time.time()) > 0.5):
			last_update[3] = time.time()
			sprites1, sprites2, sprites3, curr = mudar(curr, 2)


	if(keys[pygame.K_UP]and abs(last_update[3] - time.time()) > 0.5):
		last_update[3] = time.time()
		sprites1, sprites2, sprites3, curr = mudar(curr, 2)

	if(keys[pygame.K_DOWN] and abs(last_update[2] - time.time()) > 1):
		cred, coloc, last_update[2] = xcreditos(cred, coloc, last_update[2])

	if(keys[pygame.K_LEFT] and abs(last_update[0] - time.time()) > 2):
		credm = mcreditos(cred)
		coloc = 0
		cred = 0

	if(keys[pygame.K_RIGHT] and abs(last_update[1] - time.time()) > 4):
		last_update[1] = time.time()
		if cred >= 50:
			giro.play()
			spin_t = time.time()
			jequiti(spin_t, sprites1, sprites2, sprites3, display)
			cred = cred - 50
			if sprites1[2] == sprites2[2] == sprites3[2]:
				win.play()
				cred = cred +550
				make_it_happend = time.time()
				text_ganharcred = font.render("Voce Ganhou 500 creditos!", True, text_color)
				display.blit(text_ganharcred,(0,310))
				pygame.display.flip()
				while(abs(make_it_happend - time.time()) < 2):
					continue

				display.blit(text_ganharcred,(0,550))

		if cred < 50:
			beep.play()
			make_it_happend = time.time()
			text_Semcred = font.render("Voce precisa colocar creditos", True, text_color)
			display.blit(text_Semcred,(0,310))
			pygame.display.flip()
			while(abs(make_it_happend - time.time()) < 1.5):
				continue
	if(keys[pygame.K_t] and keys[pygame.K_a] and keys[pygame.K_d] and keys[pygame.K_s]):
		sprites1, sprites2, sprites3 = secret()

	spritess(sprites1)
	spritess(sprites2)
	spritess(sprites3)
	creditos(cred)
	pygame.display.flip()
