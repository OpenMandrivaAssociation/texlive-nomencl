Name:		texlive-nomencl
Version:	3.1a
Release:	1
Summary:	Produce lists of symbols as in nomenclature
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/nomencl
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nomencl.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nomencl.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nomencl.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Produces lists of symbols using the capabilities of the
MakeIndex program.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
