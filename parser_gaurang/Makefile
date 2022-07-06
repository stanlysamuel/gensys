setup:
	# Note: We are not using alias in this makefile because it is not compatible with it.
	export CLASSPATH=".:/usr/local/lib/antlr-4.10.1-complete.jar:$$CLASSPATH" ; \

run:	
	cd gsl ; \
	java -jar /usr/local/lib/antlr-4.10.1-complete.jar -Dlanguage=Python3 -visitor gsl.g4 ;\
	/home/gaurang/.local/bin/pygrun gsl prog $(FILE) ;\


get_ps:
	export CLASSPATH=".:/usr/local/lib/antlr-4.10.1-complete.jar:$$CLASSPATH" ; \
	cd gsl/ ; \
	java -jar /usr/local/lib/antlr-4.10.1-complete.jar -visitor gsl.g4 ; \
	javac gsl*.java; \
	java org.antlr.v4.gui.TestRig gsl prog -ps gslast.ps $(FILE); \
	ps2pdf "gslast.ps" "gslast.pdf"; \
	mv  gslast.ps gslast.pdf ../benchmarks/ ; \
	rm *.class; \
	rm *.java; \
	
	