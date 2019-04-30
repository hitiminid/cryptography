
# CONFIG_FILE = `data.json`

KEY_PASS=`cat data.json       | grep store_key      | cut -d ":" -f2 | cut -d " " -f2 | sed 's/\"//g' | sed 's/\,//g'`
STORE_PASS=`cat data.json     | grep store_password | cut -d ":" -f2 | cut -d " " -f2 | sed 's/\"//g' | sed 's/\,//g'`
KEY_STORE_NAME=`cat data.json | grep store_name     | cut -d ":" -f2 | cut -d " " -f2 | sed 's/\"//g' | sed 's/\,//g'`
ALIAS=`cat data.json          | grep store_alias    | cut -d ":" -f2 | cut -d " " -f2 | sed 's/\"//g' | sed 's/\,//g'`

all: key_gen

key_gen:
	@keytool \
		-genseckey \
		-keypass $(KEY_PASS) \
		-storepass $(STORE_PASS) \
		-alias $(ALIAS) \
		-keyalg aes \
		-keysize 256 \
		-storetype jceks \
		-keystore $(KEY_STORE_NAME)

key_list:
	@echo "Password: $(KEY_PASS)"
	@keytool \
		-list \
		-keystore $(KEY_STORE_NAME)

key_remove:
	rm $(KEY_STORE_NAME)

