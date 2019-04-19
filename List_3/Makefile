
STORE_PASS=`cat config | grep store_pass | cut -d ":" -f2 | cut -d " " -f2`
KEY_PASS=`cat config | grep key_store_password | cut -d ":" -f2 | cut -d " " -f2`
KEY_STORE_NAME=`cat config | grep key_store_name | cut -d ":" -f2 | cut -d " " -f2`

all: key_gen

key_gen:
	@keytool \
		-genseckey \
		-keypass $(KEY_PASS) \
		-storepass $(STORE_PASS) \
		-alias test1key \
		-keyalg AES \
		-keysize 128 \
		-storetype pkcs12 \
		-keystore $(KEY_STORE_NAME)

key_list:
	@echo "When prompted, insert password: $(KEY_PASS)"
	@keytool \
		-list \
		-keystore $(KEY_STORE_NAME)

key_remove:
	rm $(KEY_STORE_NAME)

run:
	./$(OUTPUT)
