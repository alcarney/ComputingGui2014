PYTHON_FLAGS = -lpthread -ldl -lutil -lm -lpython2.7 -Xlinker -export-dynamic

UI.o:
	$(CC) -c UI.cpp $(PYTHON_FLAGS)

clean: 
	rm *.o
