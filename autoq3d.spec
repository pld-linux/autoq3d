Summary:	autoq3d - complete 3D modeling application for computing aided drafting in three dimensions
Summary(pl.UTF-8):	autoq3d - pełna aplikacja CAD do modelowania 3D
Name:		AutoQ3D
Version:	1.20
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://dl.sourceforge.net/autoq3d/%{name}-v%{version}sourceLinux.zip
# Source0-md5:	cccd22e1c068651c8ad7c0831acd2aba
#Patch0:	%{name}-DESTDIR.patch
URL:		http://autoq3d.ecuadra.com/
BuildRequires:	Mesa-libGL-devel
BuildRequires:	QtGui-devel
BuildRequires:	QtOpenGL-devel
BuildRequires:	qt4-build >= 4.3.3-3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
autoq3d - complete 3D modeling application for computing aided
drafting in three dimensions.

%description -l pl.UTF-8
autoq3d to pełna aplikacja CAD do modelowania 3D.

%prep
%setup -q -n %{name}

%build
QTDIR=/usr; export QTDIR
qmake-qt4 -o Makefile AutoQ3D.pro

%{__make} \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with ldconfig}
%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
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
