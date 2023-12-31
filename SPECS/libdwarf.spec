%define soversion 1
%define soname libdwarf.so.%{soversion}
%define sofullname libdwarf.so.%{soversion}.%{version}.0

Name:          libdwarf
Version:       20180129
Release:       4%{?dist}
Summary:       Library to access the DWARF Debugging file format 
Group:         Development/Libraries

License:       LGPLv2
URL:           http://www.prevanders.net/dwarf.html
Source0:       http://www.prevanders.net/%{name}-%{version}.tar.gz
# Link libdwarf against libelf
Patch0:        libdwarf-libelf.patch

BuildRequires: gcc binutils-devel elfutils-libelf-devel

%package devel
Summary:       Library and header files of libdwarf
Group:         Development/Libraries
License:       LGPLv2
Requires:      %{name} = %{version}-%{release}

%package static
Summary:       Static libdwarf library
Group:         Development/Libraries
License:       LGPLv2
Requires:      %{name}-devel = %{version}-%{release}

%package tools
Summary:       Tools for accessing DWARF debugging information
Group:         Development/Tools
License:       GPLv2
Requires:      %{name} = %{version}-%{release}

%description
Library to access the DWARF debugging file format which supports
source level debugging of a number of procedural languages, such as C, C++,
and Fortran.  Please see http://www.dwarfstd.org for DWARF specification.

%description static
Static libdwarf library.

%description devel
Development package containing library and header files of libdwarf.

%description tools
C++ version of dwarfdump (dwarfdump2) command-line utilities 
to access DWARF debug information.

%prep
%autosetup -p1 -n dwarf-%{version}

%build
%configure --enable-shared
LD_LIBRARY_PATH="../libdwarf" make %{?_smp_mflags} SONAME="%{soname}"

%install
install -pDm 0644 libdwarf/dwarf.h         %{buildroot}%{_includedir}/libdwarf/dwarf.h
install -pDm 0644 libdwarf/libdwarf.a      %{buildroot}%{_libdir}/libdwarf.a

install -pDm 0644 libdwarf/libdwarf.h      %{buildroot}%{_includedir}/libdwarf/libdwarf.h
install -pDm 0755 libdwarf/libdwarf.so     %{buildroot}%{_libdir}/%{sofullname}
ln      -s        %{sofullname}            %{buildroot}%{_libdir}/%{soname}
ln      -s        %{sofullname}            %{buildroot}%{_libdir}/libdwarf.so
install -pDm 0755 dwarfdump/dwarfdump      %{buildroot}%{_bindir}/dwarfdump

%files
%doc libdwarf/ChangeLog libdwarf/README
%license libdwarf/COPYING libdwarf/LIBDWARFCOPYRIGHT libdwarf/LGPL.txt
%{_libdir}/libdwarf.so.*

%files static
%{_libdir}/libdwarf.a

%files devel
%doc libdwarf/*.pdf
%{_includedir}/libdwarf
%{_libdir}/libdwarf.so

%files tools
%doc dwarfdump/README dwarfdump/ChangeLog
%license dwarfdump/COPYING dwarfdump/DWARFDUMPCOPYRIGHT dwarfdump/GPL.txt
%{_bindir}/dwarfdump

%changelog
* Sun Feb 18 2018 Tom Hughes <tom@compton.nu> - 20180129-4
- Require gcc

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20180129-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 30 2018 Tom Hughes <tom@compton.nu> - 20180129-2
- Drop ldconfig scriptlets

* Tue Jan 30 2018 Tom Hughes <tom@compton.nu> - 20180129-1
- Update to 20180129 upstream release

* Tue Jan 23 2018 Tom Hughes <tom@compton.nu> - 20170709-4
- Link libdwarf against libelf

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20170709-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20170709-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 10 2017 Tom Hughes <tom@compton.nu> - 20170709-1
- Update to 20170709 upstream release

* Mon Apr 17 2017 Tom Hughes <tom@compton.nu> - 20170416-1
- Update to 20170416 upstream release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20161124-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Nov 25 2016 Tom Hughes <tom@compton.nu> - 20161124-1
- Update to 20161124 upstream release

* Sun Oct 23 2016 Tom Hughes <tom@compton.nu> - 20161021-1
- Update to 20161021 upstream release

* Sun Oct  2 2016 Tom Hughes <tom@compton.nu> - 20161001-1
- Update to 20161001 upstream release

* Fri Sep 30 2016 Tom Hughes <tom@compton.nu> - 20160929-1
- Update to 20160929 upstream release

* Mon Sep 26 2016 Tom Hughes <tom@compton.nu> - 20160923-1
- Update to 20160923 upstream release

* Wed Jun 15 2016 Tom Hughes <tom@compton.nu> - 20160613-1
- Update to 20160613 upstream release

* Sun May  8 2016 Tom Hughes <tom@compton.nu> - 20160507-1
- Update to 20160507 upstream release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20160115-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 16 2016 Tom Hughes <tom@compton.nu> - 20160115-1
- Update to 20160116 upstream release

* Wed Dec 30 2015 Tom Hughes <tom@compton.nu> - 20151114-3
- Add upstream patch for crash with debug sections marked NOBITS

* Wed Dec  9 2015 Tom Hughes <tom@compton.nu> - 20151114-2
- Add upstream patch for crash reading corrupt DWARF data

* Sun Nov 15 2015 Tom Hughes <tom@compton.nu> - 20151114-1
- Update to 20151114 upstream release

* Wed Sep 16 2015 Tom Hughes <tom@compton.nu> - 20150915-1
- Update to 20150915 upstream release

* Mon Sep 14 2015 Tom Hughes <tom@compton.nu> - 20150913-1
- Update to 20150913 upstream release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20150507-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May  8 2015 Tom Hughes <tom@compton.nu> - 20150507-1
- Update to 20150507 upstream release

* Mon Apr 20 2015 Tom Hughes <tom@compton.nu> - 20150310-4
- Drop PPC linker bug patch, as the bug is now fixed
- Re-enable hardended builds (was the same bug)

* Wed Apr 15 2015 Jaromir Capik <jcapik@redhat.com> - 20150310-3
- ppc linker bug workaround (#1208467)

* Thu Mar 12 2015 Tom Hughes <tom@compton.nu> - 20150310-2
- Disable hardened builds for now
- Drop explicit CFLAGS as %%configure sets them anyway

* Thu Mar 12 2015 Tom Hughes <tom@compton.nu> - 20150310-1
- Update to 20150310 upstream release

* Mon Jan 19 2015 Tom Hughes <tom@compton.nu> - 20150115-1
- Update to 20150115 upstream release

* Wed Jan 14 2015 Tom Hughes <tom@compton.nu> - 20150112-1
- Update to 20150112 upstream release
- Switch back to dwarfdump, as dwarfdump2 is deprecated upstream

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20140805-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Aug  6 2014 Tom Hughes <tom@compton.nu> - 20140805-1
- Update to 20140805 upstream release

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20140519-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 22 2014 Tom Hughes <tom@compton.nu> - 20140519-1
- Update to 20140519 upstream release

* Wed Apr 16 2014 Tom Hughes <tom@compton.nu> - 20140413-1
- Update to 20140413 upstream release

* Sun Feb  9 2014 Tom Hughes <tom@compton.nu> - 20140208-1
- Update to 20140208 upstream release

* Tue Feb  4 2014 Tom Hughes <tom@compton.nu> - 20140131-2
- Link libdwarf.so with libelf

* Sun Feb  2 2014 Tom Hughes <tom@compton.nu> - 20140131-1
- Update to 20140131 upstream release

* Tue Jan  7 2014 Tom Hughes <tom@compton.nu> - 20130729-2
- Update upstream URLs to point at new site

* Wed Jul 31 2013 Tom Hughes <tom@compton.nu> - 20130729-1
- Update to 20130729 release

* Fri Feb  8 2013 Tom Hughes <tom@compton.nu> - 20130207-1
- Update to 20130207 release

* Sun Jan 27 2013 Tom Hughes <tom@compton.nu> - 20130126-1
- Update to 20130126 release
- Revert soname to libdwarf.so.0

* Sat Jan 26 2013 Tom Hughes <tom@compton.nu> - 20130125-1
- Update to 20130125 release
- Bump soname to libdwarf.so.1

* Mon Dec  3 2012 Tom Hughes <tom@compton.nu> - 20121130-1
- Update to 20121130 release

* Thu Nov 29 2012 Tom Hughes <tom@compton.nu> - 20121127-1
- Update to 20121127 release

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20120410-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jul 13 2012 Tom Hughes <tom@compton.nu> - 20120410-1
- Update to 20120410 release
- Drop the 0. from the version - the dates are the upstream versions
- Remove explicit dependencies on elfutils-libelf

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20110612-3
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20110612-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jul 13 2011 Parag Nemade <paragn AT fedoraproject DOT org> - 0.20110612-1
- Update to 20110612 release

* Wed Mar 09 2011 Parag Nemade <paragn AT fedoraproject DOT org> - 0.20110113-1
- Update to 20110113 release

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20100629-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jul 06 2010 Parag Nemade <paragn AT fedoraproject.org> - 0.20100629-1
- Update to 20100629 release
- Add -static subpackage as request in rh#586807

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20090324-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Mar 31 2009 - Suravee Suthikulpanit <suravee.suthikulpanit@amd.com>
- 0.20090324-4
- Adding _smp_mflags for libdwarf build
- Move CFLAGS override from configure to make
 
* Mon Mar 30 2009 - Suravee Suthikulpanit <suravee.suthikulpanit@amd.com>
- 0.20090324-3
- Remove AutoreqProv no

* Thu Mar 26 2009 - Suravee Suthikulpanit <suravee.suthikulpanit@amd.com>
- 0.20090324-2
- Drop the C implementation of dwarfdump. (dwarfdump1)
- Since the doc package is small, we combined the contents into the devel package.
- Fix the version string.
- Drop the static library.
- Add release number to "Requires".
- Fix licensing (v2 instead of v2+)
- Change linking for libdwarf.so and libdwarf.so.0

* Wed Mar 25 2009 - Suravee Suthikulpanit <suravee.suthikulpanit@amd.com>
- 20090324-1
- Initial Revision
