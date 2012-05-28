# NOTE: Please do not edit this file, it was auto generated by jhconvert
#       See http://wiki.sugarlabs.org/go/Deployment_Team/jhconvert for details

Name:		gstreamer0.10-espeak
Version:	0.3.5
Release:	%mkrel 1
Summary:	Simple gstreamer plugin to use espeak by way of sound source
License:	LGPLv2+
Group:		Sound
Url:		http://sugarlabs.org/go/DevelopmentTeam/gst-plugins-espeak
Source:		http://download.sugarlabs.org/sources/honey/gst-plugins-espeak/gst-plugins-espeak-%{version}.tar.gz
Requires:	espeak
Requires:	gstreamer0.10-plugins-base
Requires:	gstreamer0.10-plugins-good
Requires:	gstreamer

BuildRequires:	libespeak-devel
BuildRequires:	pkgconfig(gstreamer-0.10)
BuildRequires:	pkgconfig(gstreamer-plugins-base-0.10)

%description
Simple gstreamer plugin to use espeak by way of sound source.
It was developed to simplify espeak usage in Sugar Speak activity.

%prep
%setup -q -n gst-plugins-espeak-%{version}
sed -i 's/NANO=1/NANO=0/g' configure

%build
%configure2_5x
%make

%install
%__rm -rf %{buildroot}
%makeinstall_std

%clean
%__rm -rf %{buildroot}

%files
%doc AUTHORS COPYING NEWS README
%{_libdir}/gstreamer*/*

