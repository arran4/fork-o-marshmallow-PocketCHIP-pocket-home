include Makefile

WifiTest_TARGET := wifitest
WifiTest_BLDCMD = $(CXX) -o $(JUCE_OUTDIR)/$(WifiTest_TARGET) $(WifiTest_OBJECTS) $(JUCE_LDFLAGS) $(RESOURCES) $(TARGET_ARCH)
WifiTest_CLEANCMD = rm -f $(JUCE_OUTDIR)/$(WifiTest_TARGET)

WifiTest_OBJECTS := \
  $(JUCE_OBJDIR)/WifiStatusNM_92fce0ef.o \
  $(JUCE_OBJDIR)/WifiStatusJson_715858f8.o \
  $(JUCE_OBJDIR)/WifiStatus_30949170.o \
  $(JUCE_OBJDIR)/Utils_e4b11b92.o \
  $(JUCE_OBJDIR)/juce_core_75b14332.o \
  $(JUCE_OBJDIR)/juce_data_structures_72d3da2c.o \
  $(JUCE_OBJDIR)/juce_events_d2be882c.o \
  $(JUCE_OBJDIR)/juce_graphics_9c18891e.o \
  $(JUCE_OBJDIR)/juce_gui_basics_8a6da59c.o \
  $(JUCE_OBJDIR)/WifiTest_1459807182.o \

$(JUCE_OUTDIR)/$(WifiTest_TARGET): $(WifiTest_OBJECTS) $(RESOURCES)
	@echo Linking wifitest
	-@mkdir -p $(JUCE_BINDIR)
	-@mkdir -p $(JUCE_LIBDIR)
	-@mkdir -p $(JUCE_OUTDIR)
	@$(WifiTest_BLDCMD)

$(JUCE_OUTDIR)/$(WifiTest_TARGET)-clean:
	@echo Cleaning wifitest
	@$(WifiTest_CLEANCMD)
	@$(CLEANCMD)

$(JUCE_OBJDIR)/WifiTest_1459807182.o: ../../Source/WifiTest.cpp
	-@mkdir -p $(JUCE_OBJDIR)
	@echo "Compiling WifiTest.cpp"
	@$(CXX) $(JUCE_CXXFLAGS) -o "$@" -c "$<"
