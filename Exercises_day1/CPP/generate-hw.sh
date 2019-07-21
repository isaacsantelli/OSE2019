#!/usr/bin/env bash

HWNAME="hw10"
WUNAME="warmup10"

mkdir "$HWNAME"
cd "$HWNAME" || exit

touch "$HWNAME"{.c,.h,_main.c}
touch "$WUNAME"{.c,.h,_main.c}

CAPS_HWNAME="HW10"
CAPS_WUNAME="WARMUP10"

function gen_header() {
	cat <<- EOF > "$1".h
	#ifndef ${2}_H
	#define ${2}_H

	#include <stdio.h>
	#include <stdlib.h>

	#endif
	EOF
}

function gen_cfile() {
	cat <<- EOF > "$1".c
	#include <stdio.h>
	#include <stdlib.h>
	#include <string.h>
	#include <stdbool.h>
	#include "${1}.h"
	EOF
}

function gen_mainfile() {
	cat <<- EOF > "$1"_main.c
	#include <stdio.h>
	#include <stdlib.h>
	#include <string.h>
	#include <stdbool.h>
	#include "${1}.h"

	int main(int argc, char const *argv[])
	{
	   /* code */
	   return 0;
	}
	EOF
}

gen_header "$HWNAME" "$CAPS_HWNAME"
gen_cfile "$HWNAME"
gen_mainfile "$HWNAME"

gen_header "$WUNAME" "$CAPS_WUNAME"
gen_cfile "$WUNAME"
gen_mainfile "$WUNAME"

cat << EOF > Makefile
${WUNAME}: ${WUNAME}.c ${WUNAME}_main.c ${WUNAME}.h
	clang ${WUNAME}_main.c ${WUNAME}.c -o ${WUNAME}

${HWNAME}: ${HWNAME}.h ${HWNAME}.c ${HWNAME}_main.c
	clang -Wall -o ${HWNAME} ${HWNAME}.c ${HWNAME}_main.c
EOF
