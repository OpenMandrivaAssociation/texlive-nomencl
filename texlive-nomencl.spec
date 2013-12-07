# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/nomencl
# catalog-date 2007-01-12 00:17:35 +0100
# catalog-license lppl
# catalog-version 3.1a
Name:		texlive-nomencl
Version:	3.1a
Release:	6
Summary:	Produce lists of symbols as in nomenclature
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/nomencl
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nomencl.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nomencl.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nomencl.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Produces lists of symbols using the capabilities of the
MakeIndex program.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/makeindex/nomencl/nomencl.ist
%{_texmfdistdir}/tex/latex/nomencl/nomencl.sty
%{_texmfdistdir}/tex/latex/nomencl/sample01.cfg
%{_texmfdistdir}/tex/latex/nomencl/sample02.cfg
%{_texmfdistdir}/tex/latex/nomencl/sample04.cfg
%{_texmfdistdir}/tex/latex/nomencl/sample05.cfg
%doc %{_texmfdistdir}/doc/latex/nomencl/README
%doc %{_texmfdistdir}/doc/latex/nomencl/nomencl.pdf
#- source
%doc %{_texmfdistdir}/source/latex/nomencl/nomencl.drv
%doc %{_texmfdistdir}/source/latex/nomencl/nomencl.dtx
%doc %{_texmfdistdir}/source/latex/nomencl/nomencl.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar makeindex tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 3.1a-2
+ Revision: 754354
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 3.1a-1
+ Revision: 719126
- texlive-nomencl
- texlive-nomencl
- texlive-nomencl
- texlive-nomencl

