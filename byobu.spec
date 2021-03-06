#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : byobu
Version  : 5.129
Release  : 3
URL      : https://launchpad.net/byobu/trunk/5.129/+download/byobu_5.129.orig.tar.gz
Source0  : https://launchpad.net/byobu/trunk/5.129/+download/byobu_5.129.orig.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: byobu-bin = %{version}-%{release}
Requires: byobu-data = %{version}-%{release}
Requires: byobu-license = %{version}-%{release}
Requires: byobu-man = %{version}-%{release}

%description
For more information about this package, please see:
* http://byobu.org
If Byobu is not packaged for your Linux or UNIX OS, or if you do not have
administrative privileges in order to install Byobu, you may be able to
install locally, using the following instructions...

%package bin
Summary: bin components for the byobu package.
Group: Binaries
Requires: byobu-data = %{version}-%{release}
Requires: byobu-license = %{version}-%{release}

%description bin
bin components for the byobu package.


%package data
Summary: data components for the byobu package.
Group: Data

%description data
data components for the byobu package.


%package doc
Summary: doc components for the byobu package.
Group: Documentation
Requires: byobu-man = %{version}-%{release}

%description doc
doc components for the byobu package.


%package license
Summary: license components for the byobu package.
Group: Default

%description license
license components for the byobu package.


%package man
Summary: man components for the byobu package.
Group: Default

%description man
man components for the byobu package.


%prep
%setup -q -n byobu-5.129
cd %{_builddir}/byobu-5.129

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1605245550
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1605245550
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/byobu
cp %{_builddir}/byobu-5.129/COPYING %{buildroot}/usr/share/package-licenses/byobu/842745cb706f8f2126506f544492f7a80dbe29b3
%make_install

%files
%defattr(-,root,root,-)
/usr/lib/byobu/apport
/usr/lib/byobu/arch
/usr/lib/byobu/battery
/usr/lib/byobu/color
/usr/lib/byobu/cpu_count
/usr/lib/byobu/cpu_freq
/usr/lib/byobu/cpu_temp
/usr/lib/byobu/custom
/usr/lib/byobu/date
/usr/lib/byobu/disk
/usr/lib/byobu/disk_io
/usr/lib/byobu/distro
/usr/lib/byobu/entropy
/usr/lib/byobu/fan_speed
/usr/lib/byobu/hostname
/usr/lib/byobu/include/colors
/usr/lib/byobu/include/common
/usr/lib/byobu/include/config.py
/usr/lib/byobu/include/constants
/usr/lib/byobu/include/cycle-status
/usr/lib/byobu/include/dirs
/usr/lib/byobu/include/icons
/usr/lib/byobu/include/mondrian
/usr/lib/byobu/include/notify_osd
/usr/lib/byobu/include/select-session.py
/usr/lib/byobu/include/shutil
/usr/lib/byobu/include/tmux-detach-all-but-current-client
/usr/lib/byobu/include/tmux-send-command-to-all-panes
/usr/lib/byobu/include/tmux-send-command-to-all-windows
/usr/lib/byobu/include/toggle-utf8
/usr/lib/byobu/ip_address
/usr/lib/byobu/load_average
/usr/lib/byobu/logo
/usr/lib/byobu/mail
/usr/lib/byobu/memory
/usr/lib/byobu/menu
/usr/lib/byobu/network
/usr/lib/byobu/processes
/usr/lib/byobu/raid
/usr/lib/byobu/reboot_required
/usr/lib/byobu/release
/usr/lib/byobu/services
/usr/lib/byobu/session
/usr/lib/byobu/swap
/usr/lib/byobu/time
/usr/lib/byobu/time_binary
/usr/lib/byobu/time_utc
/usr/lib/byobu/trash
/usr/lib/byobu/updates_available
/usr/lib/byobu/uptime
/usr/lib/byobu/users
/usr/lib/byobu/whoami
/usr/lib/byobu/wifi_quality

%files bin
%defattr(-,root,root,-)
/usr/bin/byobu
/usr/bin/byobu-config
/usr/bin/byobu-ctrl-a
/usr/bin/byobu-disable
/usr/bin/byobu-disable-prompt
/usr/bin/byobu-enable
/usr/bin/byobu-enable-prompt
/usr/bin/byobu-export
/usr/bin/byobu-janitor
/usr/bin/byobu-keybindings
/usr/bin/byobu-launch
/usr/bin/byobu-launcher
/usr/bin/byobu-launcher-install
/usr/bin/byobu-launcher-uninstall
/usr/bin/byobu-layout
/usr/bin/byobu-prompt
/usr/bin/byobu-quiet
/usr/bin/byobu-reconnect-sockets
/usr/bin/byobu-screen
/usr/bin/byobu-select-backend
/usr/bin/byobu-select-profile
/usr/bin/byobu-select-session
/usr/bin/byobu-shell
/usr/bin/byobu-silent
/usr/bin/byobu-status
/usr/bin/byobu-status-detail
/usr/bin/byobu-tmux
/usr/bin/byobu-ugraph
/usr/bin/byobu-ulevel
/usr/bin/col1
/usr/bin/ctail
/usr/bin/manifest
/usr/bin/purge-old-kernels
/usr/bin/vigpg
/usr/bin/wifi-status

%files data
%defattr(-,root,root,-)
/usr/share/byobu/desktop/byobu.desktop
/usr/share/byobu/desktop/byobu.desktop.old
/usr/share/byobu/keybindings/common
/usr/share/byobu/keybindings/f-keys
/usr/share/byobu/keybindings/f-keys.screen
/usr/share/byobu/keybindings/f-keys.screen.disable
/usr/share/byobu/keybindings/f-keys.tmux
/usr/share/byobu/keybindings/f-keys.tmux.disable
/usr/share/byobu/keybindings/mouse.tmux.disable
/usr/share/byobu/keybindings/mouse.tmux.enable
/usr/share/byobu/keybindings/none
/usr/share/byobu/keybindings/tmux-screen-keys.conf
/usr/share/byobu/pixmaps/byobu.svg
/usr/share/byobu/profiles/NONE
/usr/share/byobu/profiles/bashrc
/usr/share/byobu/profiles/byoburc
/usr/share/byobu/profiles/common
/usr/share/byobu/profiles/dircolors
/usr/share/byobu/profiles/screenrc
/usr/share/byobu/profiles/tmux
/usr/share/byobu/profiles/tmuxrc
/usr/share/byobu/status/status
/usr/share/byobu/status/statusrc
/usr/share/byobu/tests/byobu-time-notifications
/usr/share/byobu/windows/common
/usr/share/dbus-1/services/us.kirkland.terminals.byobu.service

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/byobu/*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/byobu/842745cb706f8f2126506f544492f7a80dbe29b3

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/byobu-config.1
/usr/share/man/man1/byobu-ctrl-a.1
/usr/share/man/man1/byobu-disable-prompt.1
/usr/share/man/man1/byobu-disable.1
/usr/share/man/man1/byobu-enable-prompt.1
/usr/share/man/man1/byobu-enable.1
/usr/share/man/man1/byobu-export.1
/usr/share/man/man1/byobu-janitor.1
/usr/share/man/man1/byobu-keybindings.1
/usr/share/man/man1/byobu-launch.1
/usr/share/man/man1/byobu-launcher-install.1
/usr/share/man/man1/byobu-launcher-uninstall.1
/usr/share/man/man1/byobu-launcher.1
/usr/share/man/man1/byobu-layout.1
/usr/share/man/man1/byobu-prompt.1
/usr/share/man/man1/byobu-quiet.1
/usr/share/man/man1/byobu-reconnect-sockets.1
/usr/share/man/man1/byobu-screen.1
/usr/share/man/man1/byobu-select-backend.1
/usr/share/man/man1/byobu-select-profile.1
/usr/share/man/man1/byobu-select-session.1
/usr/share/man/man1/byobu-shell.1
/usr/share/man/man1/byobu-silent.1
/usr/share/man/man1/byobu-status-detail.1
/usr/share/man/man1/byobu-status.1
/usr/share/man/man1/byobu-tmux.1
/usr/share/man/man1/byobu-ugraph.1
/usr/share/man/man1/byobu-ulevel.1
/usr/share/man/man1/byobu.1
/usr/share/man/man1/col1.1
/usr/share/man/man1/ctail.1
/usr/share/man/man1/manifest.1
/usr/share/man/man1/purge-old-kernels.1
/usr/share/man/man1/vigpg.1
/usr/share/man/man1/wifi-status.1
