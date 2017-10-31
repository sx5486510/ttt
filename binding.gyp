{
	"targets" :[
		{
			"target_name": "cryptopp",
			"sources": [
			"keyring.cpp",
			"cryptopp/misc.cpp",
			],
			"include_dirs": [
			".",
                "<!(node -e \"require('nan')\")",
			],
			"libraries": ["../cryptopp/libcryptopp.a"],
			"cflags!": ["-fno-exceptions"],
			"cflags_cc!": ["-fno-exceptions", "-fno-rtti"],
			"cflags_cc+": ["-frtti"],
			"conditions": [
				['OS=="mac"', {
					"xcode_settings": {
						"GCC_ENABLE_CPP_EXCEPTIONS": "YES",
						"GCC_ENABLE_CPP_RTTI": "YES",
						"OTHER_CFLAGS": ["-mmacosx-version-min=10.7", "-std=c++11", "-stdlib=libc++"],
						"OTHER_CPLUSPLUSFLAGS": ["-mmacosx-version-min=10.7", "-std=c++11", "-stdlib=libc++"]
					}
				}]
			]
		}
	]
}
