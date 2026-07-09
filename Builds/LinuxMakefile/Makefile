# Automatically generated makefile, created by the Projucer
# Don't edit this file! Your changes will be overwritten when you re-save the Projucer project!

# (this disables dependency generation if multiple architectures are set)
DEPFLAGS := $(if $(word 2, $(TARGET_ARCH)), , -MMD)

ifndef STRIP
  STRIP=strip
endif

ifndef AR
  AR=ar
endif

ifndef CONFIG
  CONFIG=Debug
endif

ifeq ($(CONFIG),Debug)
  JUCE_BINDIR := build
  JUCE_LIBDIR := build
  JUCE_OBJDIR := build/intermediate/Debug
  JUCE_OUTDIR := ../../build/Debug

  ifeq ($(TARGET_ARCH),)
    TARGET_ARCH := -march=native
  endif

  JUCE_CPPFLAGS := $(DEPFLAGS) -DLINUX=1 -DDEBUG=1 -D_DEBUG=1 -DJUCER_LINUX_MAKE_6D53C8B4=1 -DJUCE_APP_VERSION=0.0.1 -DJUCE_APP_VERSION_HEX=0x1 $(shell pkg-config --cflags NetworkManager libnm-glib alsa freetype2) -pthread -I../../JuceLibraryCode -I../../deps/JUCE/modules
  JUCE_CFLAGS += $(CFLAGS) $(JUCE_CPPFLAGS) $(TARGET_ARCH) -g -ggdb -O0
  JUCE_CXXFLAGS += $(CXXFLAGS) $(JUCE_CFLAGS) -std=c++11
  JUCE_LDFLAGS += $(LDFLAGS) $(TARGET_ARCH) -L$(JUCE_BINDIR) -L$(JUCE_LIBDIR) -L/usr/X11R6/lib/ $(shell pkg-config --libs NetworkManager libnm-glib alsa freetype2) -lX11 -lXext -lXinerama -ldl -lfreetype -lpthread -lrt

  TARGET := pocket-home
  BLDCMD = $(CXX) -o $(JUCE_OUTDIR)/$(TARGET) $(OBJECTS) $(JUCE_LDFLAGS) $(RESOURCES) $(TARGET_ARCH)
  CLEANCMD = rm -rf $(JUCE_OUTDIR)/$(TARGET) $(JUCE_OBJDIR)
endif

ifeq ($(CONFIG),Release)
  JUCE_BINDIR := build
  JUCE_LIBDIR := build
  JUCE_OBJDIR := build/intermediate/Release
  JUCE_OUTDIR := ../../build/Release

  ifeq ($(TARGET_ARCH),)
    TARGET_ARCH := -march=native
  endif

  JUCE_CPPFLAGS := $(DEPFLAGS) -DLINUX=1 -DNDEBUG=1 -DJUCER_LINUX_MAKE_6D53C8B4=1 -DJUCE_APP_VERSION=0.0.1 -DJUCE_APP_VERSION_HEX=0x1 $(shell pkg-config --cflags NetworkManager libnm-glib alsa freetype2) -pthread -I../../JuceLibraryCode -I../../deps/JUCE/modules
  JUCE_CFLAGS += $(CFLAGS) $(JUCE_CPPFLAGS) $(TARGET_ARCH) -O3
  JUCE_CXXFLAGS += $(CXXFLAGS) $(JUCE_CFLAGS) -std=c++11
  JUCE_LDFLAGS += $(LDFLAGS) $(TARGET_ARCH) -L$(JUCE_BINDIR) -L$(JUCE_LIBDIR) -fvisibility=hidden -L/usr/X11R6/lib/ $(shell pkg-config --libs NetworkManager libnm-glib alsa freetype2) -lX11 -lXext -lXinerama -ldl -lfreetype -lpthread -lrt -lcrypto

  TARGET := pocket-home
  BLDCMD = $(CXX) -o $(JUCE_OUTDIR)/$(TARGET) $(OBJECTS) $(JUCE_LDFLAGS) $(RESOURCES) $(TARGET_ARCH)
  CLEANCMD = rm -rf $(JUCE_OUTDIR)/$(TARGET) $(JUCE_OBJDIR)
endif

OBJECTS := \
  $(JUCE_OBJDIR)/OverlaySpinner_80e19ab2.o \
  $(JUCE_OBJDIR)/AdvancedSettingsPage_6068151d.o \
  $(JUCE_OBJDIR)/ClockMonitor_d7cf07f5.o \
  $(JUCE_OBJDIR)/DateTimePage_7bef7c53.o \
  $(JUCE_OBJDIR)/InputSettingsPage_dcd5c19d.o \
  $(JUCE_OBJDIR)/PersonalizePageComponent_bc639603.o \
  $(JUCE_OBJDIR)/SettingsPageLogin_497cef18.o \
  $(JUCE_OBJDIR)/Grid_a461bccf.o \
  $(JUCE_OBJDIR)/PowerPageFelComponent_e97c8ca5.o \
  $(JUCE_OBJDIR)/LibraryPageComponent_6532e93c.o \
  $(JUCE_OBJDIR)/PowerPageComponent_4a26c732.o \
  $(JUCE_OBJDIR)/BatteryMonitor_37302b96.o \
  $(JUCE_OBJDIR)/WifiStatusJson_715858f8.o \
  $(JUCE_OBJDIR)/WifiStatusNM_92fce0ef.o \
  $(JUCE_OBJDIR)/WifiStatus_30949170.o \
  $(JUCE_OBJDIR)/LauncherComponent_8a29041e.o \
  $(JUCE_OBJDIR)/PageStackComponent_8da9db4d.o \
  $(JUCE_OBJDIR)/SwitchComponent_a904080a.o \
  $(JUCE_OBJDIR)/Utils_e4b11b92.o \
  $(JUCE_OBJDIR)/LauncherBarComponent_b69b173.o \
  $(JUCE_OBJDIR)/AppsPageComponent_7872953d.o \
  $(JUCE_OBJDIR)/PokeLookAndFeel_55885106.o \
  $(JUCE_OBJDIR)/MainComponent_a6ffb4a5.o \
  $(JUCE_OBJDIR)/SettingsPageComponent_10c3e5ac.o \
  $(JUCE_OBJDIR)/SettingsPageBluetoothComponent_e05cbdea.o \
  $(JUCE_OBJDIR)/SettingsPageWifiComponent_10168397.o \
  $(JUCE_OBJDIR)/IconSliderComponent_f4b4d044.o \
  $(JUCE_OBJDIR)/Main_90ebc5c2.o \
  $(JUCE_OBJDIR)/BinaryData_ce4232d4.o \
  $(JUCE_OBJDIR)/juce_core_75b14332.o \
  $(JUCE_OBJDIR)/juce_data_structures_72d3da2c.o \
  $(JUCE_OBJDIR)/juce_events_d2be882c.o \
  $(JUCE_OBJDIR)/juce_graphics_9c18891e.o \
  $(JUCE_OBJDIR)/juce_gui_basics_8a6da59c.o \

.PHONY: clean

$(JUCE_OUTDIR)/$(TARGET): check-pkg-config $(OBJECTS) $(RESOURCES)
	@echo Linking pocket-home
	-@mkdir -p $(JUCE_BINDIR)
	-@mkdir -p $(JUCE_LIBDIR)
	-@mkdir -p $(JUCE_OUTDIR)
	@$(BLDCMD)

check-pkg-config:
	@command -v pkg-config >/dev/null 2>&1 || { echo >&2 "pkg-config not installed. Please, install it."; exit 1; }
	@pkg-config --print-errors NetworkManager libnm-glib alsa freetype2

clean:
	@echo Cleaning pocket-home
	@$(CLEANCMD)

strip:
	@echo Stripping pocket-home
	-@$(STRIP) --strip-unneeded $(JUCE_OUTDIR)/$(TARGET)

$(JUCE_OBJDIR)/OverlaySpinner_80e19ab2.o: ../../Source/OverlaySpinner.cpp
	-@mkdir -p $(JUCE_OBJDIR)
	@echo "Compiling OverlaySpinner.cpp"
	@$(CXX) $(JUCE_CXXFLAGS) -o "$@" -c "$<"

$(JUCE_OBJDIR)/AdvancedSettingsPage_6068151d.o: ../../Source/AdvancedSettingsPage.cpp
	-@mkdir -p $(JUCE_OBJDIR)
	@echo "Compiling AdvancedSettingsPage.cpp"
	@$(CXX) $(JUCE_CXXFLAGS) -o "$@" -c "$<"

$(JUCE_OBJDIR)/ClockMonitor_d7cf07f5.o: ../../Source/ClockMonitor.cpp
	-@mkdir -p $(JUCE_OBJDIR)
	@echo "Compiling ClockMonitor.cpp"
	@$(CXX) $(JUCE_CXXFLAGS) -o "$@" -c "$<"

$(JUCE_OBJDIR)/DateTimePage_7bef7c53.o: ../../Source/DateTimePage.cpp
	-@mkdir -p $(JUCE_OBJDIR)
	@echo "Compiling DateTimePage.cpp"
	@$(CXX) $(JUCE_CXXFLAGS) -o "$@" -c "$<"

$(JUCE_OBJDIR)/InputSettingsPage_dcd5c19d.o: ../../Source/InputSettingsPage.cpp
	-@mkdir -p $(JUCE_OBJDIR)
	@echo "Compiling InputSettingsPage.cpp"
	@$(CXX) $(JUCE_CXXFLAGS) -o "$@" -c "$<"

$(JUCE_OBJDIR)/PersonalizePageComponent_bc639603.o: ../../Source/PersonalizePageComponent.cpp
	-@mkdir -p $(JUCE_OBJDIR)
	@echo "Compiling PersonalizePageComponent.cpp"
	@$(CXX) $(JUCE_CXXFLAGS) -o "$@" -c "$<"

$(JUCE_OBJDIR)/SettingsPageLogin_497cef18.o: ../../Source/SettingsPageLogin.cpp
	-@mkdir -p $(JUCE_OBJDIR)
	@echo "Compiling SettingsPageLogin.cpp"
	@$(CXX) $(JUCE_CXXFLAGS) -o "$@" -c "$<"

$(JUCE_OBJDIR)/Grid_a461bccf.o: ../../Source/Grid.cpp
	-@mkdir -p $(JUCE_OBJDIR)
	@echo "Compiling Grid.cpp"
	@$(CXX) $(JUCE_CXXFLAGS) -o "$@" -c "$<"

$(JUCE_OBJDIR)/PowerPageFelComponent_e97c8ca5.o: ../../Source/PowerPageFelComponent.cpp
	-@mkdir -p $(JUCE_OBJDIR)
	@echo "Compiling PowerPageFelComponent.cpp"
	@$(CXX) $(JUCE_CXXFLAGS) -o "$@" -c "$<"

$(JUCE_OBJDIR)/LibraryPageComponent_6532e93c.o: ../../Source/LibraryPageComponent.cpp
	-@mkdir -p $(JUCE_OBJDIR)
	@echo "Compiling LibraryPageComponent.cpp"
	@$(CXX) $(JUCE_CXXFLAGS) -o "$@" -c "$<"

$(JUCE_OBJDIR)/PowerPageComponent_4a26c732.o: ../../Source/PowerPageComponent.cpp
	-@mkdir -p $(JUCE_OBJDIR)
	@echo "Compiling PowerPageComponent.cpp"
	@$(CXX) $(JUCE_CXXFLAGS) -o "$@" -c "$<"

$(JUCE_OBJDIR)/BatteryMonitor_37302b96.o: ../../Source/BatteryMonitor.cpp
	-@mkdir -p $(JUCE_OBJDIR)
	@echo "Compiling BatteryMonitor.cpp"
	@$(CXX) $(JUCE_CXXFLAGS) -o "$@" -c "$<"

$(JUCE_OBJDIR)/WifiStatusJson_715858f8.o: ../../Source/WifiStatusJson.cpp
	-@mkdir -p $(JUCE_OBJDIR)
	@echo "Compiling WifiStatusJson.cpp"
	@$(CXX) $(JUCE_CXXFLAGS) -o "$@" -c "$<"

$(JUCE_OBJDIR)/WifiStatusNM_92fce0ef.o: ../../Source/WifiStatusNM.cpp
	-@mkdir -p $(JUCE_OBJDIR)
	@echo "Compiling WifiStatusNM.cpp"
	@$(CXX) $(JUCE_CXXFLAGS) -o "$@" -c "$<"

$(JUCE_OBJDIR)/WifiStatus_30949170.o: ../../Source/WifiStatus.cpp
	-@mkdir -p $(JUCE_OBJDIR)
	@echo "Compiling WifiStatus.cpp"
	@$(CXX) $(JUCE_CXXFLAGS) -o "$@" -c "$<"

$(JUCE_OBJDIR)/LauncherComponent_8a29041e.o: ../../Source/LauncherComponent.cpp
	-@mkdir -p $(JUCE_OBJDIR)
	@echo "Compiling LauncherComponent.cpp"
	@$(CXX) $(JUCE_CXXFLAGS) -o "$@" -c "$<"

$(JUCE_OBJDIR)/PageStackComponent_8da9db4d.o: ../../Source/PageStackComponent.cpp
	-@mkdir -p $(JUCE_OBJDIR)
	@echo "Compiling PageStackComponent.cpp"
	@$(CXX) $(JUCE_CXXFLAGS) -o "$@" -c "$<"

$(JUCE_OBJDIR)/SwitchComponent_a904080a.o: ../../Source/SwitchComponent.cpp
	-@mkdir -p $(JUCE_OBJDIR)
	@echo "Compiling SwitchComponent.cpp"
	@$(CXX) $(JUCE_CXXFLAGS) -o "$@" -c "$<"

$(JUCE_OBJDIR)/Utils_e4b11b92.o: ../../Source/Utils.cpp
	-@mkdir -p $(JUCE_OBJDIR)
	@echo "Compiling Utils.cpp"
	@$(CXX) $(JUCE_CXXFLAGS) -o "$@" -c "$<"

$(JUCE_OBJDIR)/LauncherBarComponent_b69b173.o: ../../Source/LauncherBarComponent.cpp
	-@mkdir -p $(JUCE_OBJDIR)
	@echo "Compiling LauncherBarComponent.cpp"
	@$(CXX) $(JUCE_CXXFLAGS) -o "$@" -c "$<"

$(JUCE_OBJDIR)/AppsPageComponent_7872953d.o: ../../Source/AppsPageComponent.cpp
	-@mkdir -p $(JUCE_OBJDIR)
	@echo "Compiling AppsPageComponent.cpp"
	@$(CXX) $(JUCE_CXXFLAGS) -o "$@" -c "$<"

$(JUCE_OBJDIR)/PokeLookAndFeel_55885106.o: ../../Source/PokeLookAndFeel.cpp
	-@mkdir -p $(JUCE_OBJDIR)
	@echo "Compiling PokeLookAndFeel.cpp"
	@$(CXX) $(JUCE_CXXFLAGS) -o "$@" -c "$<"

$(JUCE_OBJDIR)/MainComponent_a6ffb4a5.o: ../../Source/MainComponent.cpp
	-@mkdir -p $(JUCE_OBJDIR)
	@echo "Compiling MainComponent.cpp"
	@$(CXX) $(JUCE_CXXFLAGS) -o "$@" -c "$<"

$(JUCE_OBJDIR)/SettingsPageComponent_10c3e5ac.o: ../../Source/SettingsPageComponent.cpp
	-@mkdir -p $(JUCE_OBJDIR)
	@echo "Compiling SettingsPageComponent.cpp"
	@$(CXX) $(JUCE_CXXFLAGS) -o "$@" -c "$<"

$(JUCE_OBJDIR)/SettingsPageBluetoothComponent_e05cbdea.o: ../../Source/SettingsPageBluetoothComponent.cpp
	-@mkdir -p $(JUCE_OBJDIR)
	@echo "Compiling SettingsPageBluetoothComponent.cpp"
	@$(CXX) $(JUCE_CXXFLAGS) -o "$@" -c "$<"

$(JUCE_OBJDIR)/SettingsPageWifiComponent_10168397.o: ../../Source/SettingsPageWifiComponent.cpp
	-@mkdir -p $(JUCE_OBJDIR)
	@echo "Compiling SettingsPageWifiComponent.cpp"
	@$(CXX) $(JUCE_CXXFLAGS) -o "$@" -c "$<"

$(JUCE_OBJDIR)/IconSliderComponent_f4b4d044.o: ../../Source/IconSliderComponent.cpp
	-@mkdir -p $(JUCE_OBJDIR)
	@echo "Compiling IconSliderComponent.cpp"
	@$(CXX) $(JUCE_CXXFLAGS) -o "$@" -c "$<"

$(JUCE_OBJDIR)/Main_90ebc5c2.o: ../../Source/Main.cpp
	-@mkdir -p $(JUCE_OBJDIR)
	@echo "Compiling Main.cpp"
	@$(CXX) $(JUCE_CXXFLAGS) -o "$@" -c "$<"

$(JUCE_OBJDIR)/BinaryData_ce4232d4.o: ../../JuceLibraryCode/BinaryData.cpp
	-@mkdir -p $(JUCE_OBJDIR)
	@echo "Compiling BinaryData.cpp"
	@$(CXX) $(JUCE_CXXFLAGS) -o "$@" -c "$<"

$(JUCE_OBJDIR)/juce_core_75b14332.o: ../../JuceLibraryCode/juce_core.cpp
	-@mkdir -p $(JUCE_OBJDIR)
	@echo "Compiling juce_core.cpp"
	@$(CXX) $(JUCE_CXXFLAGS) -o "$@" -c "$<"

$(JUCE_OBJDIR)/juce_data_structures_72d3da2c.o: ../../JuceLibraryCode/juce_data_structures.cpp
	-@mkdir -p $(JUCE_OBJDIR)
	@echo "Compiling juce_data_structures.cpp"
	@$(CXX) $(JUCE_CXXFLAGS) -o "$@" -c "$<"

$(JUCE_OBJDIR)/juce_events_d2be882c.o: ../../JuceLibraryCode/juce_events.cpp
	-@mkdir -p $(JUCE_OBJDIR)
	@echo "Compiling juce_events.cpp"
	@$(CXX) $(JUCE_CXXFLAGS) -o "$@" -c "$<"

$(JUCE_OBJDIR)/juce_graphics_9c18891e.o: ../../JuceLibraryCode/juce_graphics.cpp
	-@mkdir -p $(JUCE_OBJDIR)
	@echo "Compiling juce_graphics.cpp"
	@$(CXX) $(JUCE_CXXFLAGS) -o "$@" -c "$<"

$(JUCE_OBJDIR)/juce_gui_basics_8a6da59c.o: ../../JuceLibraryCode/juce_gui_basics.cpp
	-@mkdir -p $(JUCE_OBJDIR)
	@echo "Compiling juce_gui_basics.cpp"
	@$(CXX) $(JUCE_CXXFLAGS) -o "$@" -c "$<"

-include $(OBJECTS:%.o=%.d)
