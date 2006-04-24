Summary:	autoq3d - complete 3D modeling application for computing aided drafting in three dimensions
Summary(pl):	autoq3d
Name:		AutoQ3D
Version:	1.20
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://dl.sourceforge.net/autoq3d/%{name}-v%{version}sourceLinux.zip
# Source0-md5:	cccd22e1c068651c8ad7c0831acd2aba
#Patch0:	%{name}-DESTDIR.patch
URL:		http://autoq3d.ecuadra.com/
BuildRequires:	QtGui-devel
BuildRequires:	Mesa-libGL-devel
BuildRequires:	QtOpenGL-devel
BuildRequires:	qt4-build
#BuildRequires:	libtool

%description
autoq3d - complete 3D modeling application for computing aided
drafting in three dimensions.

%description -l pl

%prep
%setup -q -n %{name}

%build
QTDIR=/usr; export QTDIR
/usr/bin/qmake -o Makefile AutoQ3D.pro

%{__make} \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
#install -d $RPM_BUILD_ROOT
#install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with ldconfig}
%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%endif

%if %{with initscript}
%post init
/sbin/chkconfig --add %{name}
%service %{name} restart

%preun init
if [ "$1" = "0" ]; then
	%service -q %{name} stop
	/sbin/chkconfig --del %{name}
fi
%endif

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO

%if 0
# if _sysconfdir != /etc:
#%%dir %{_sysconfdir}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%endif

# initscript and its config
%if %{with initscript}
%attr(754,root,root) /etc/rc.d/init.d/%{name}
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/%{name}
%endif

#%{_examplesdir}/%{name}-%{version}
