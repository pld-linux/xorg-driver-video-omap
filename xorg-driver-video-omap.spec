Summary:	X.org video driver for TI OMAP graphics
Summary(pl.UTF-8):	Sterownik obrazu X.org dla układów TI OMAP
Name:		xorg-driver-video-omap
Version:	0.4.1
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-omap-%{version}.tar.bz2
# Source0-md5:	f260ca9203a4c7aa290a4b6c190000f2
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	libdrm-devel >= 2.4.36
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	rpmbuild(macros) >= 1.389
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	xorg-proto-glproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-proto-renderproto-devel
BuildRequires:	xorg-proto-videoproto-devel
BuildRequires:	xorg-proto-xextproto-devel
BuildRequires:	xorg-proto-xf86driproto-devel
BuildRequires:	xorg-proto-xproto-devel
BuildRequires:	xorg-util-util-macros >= 1.4
BuildRequires:	xorg-xserver-server-devel >= 1.3
%{?requires_xorg_xserver_videodrv}
Requires:	libdrm >= 2.4.36
Requires:	xorg-xserver-server >= 1.3
ExclusiveArch:	arm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Open-source X.org video driver for TI OMAP graphics.

Currently relies on a closed-source submodule for EXA acceleration on:
OMAP3430, OMAP3630, OMAP4430, OMAP4460, OMAP5430, OMAP5432.

%description -l pl.UTF-8
Sterownik graficzny X.org o otwartych źródłach dla układów graficznych
TI OMAP.

Obecnie do akceleracji EXA wymaga podmoduły o zamkniętych źródłach dla
układów OMAP3430, OMAP3630, OMAP4430, OMAP4460, OMAP5430, OMAP5432.

%prep
%setup -q -n xf86-video-omap-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/omap_drv.so
%{_mandir}/man4/omap.4*
