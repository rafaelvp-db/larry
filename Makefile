rebuild:
	cd ui && yarn build && cd .. && docker build -t larry .