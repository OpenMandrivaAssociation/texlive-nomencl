Name:		texlive-nomencl
Version:	61029
Release:	1
Summary:	Produce lists of symbols as in nomenclature
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/nomencl
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nomencl.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nomencl.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nomencl.source.r%{version}.tar.xz
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
%{_texmfdistdir}/makeindex/nomencl
%{_texmfdistdir}/tex/latex/nomencl
%doc %{_texmfdistdir}/doc/latex/nomencl
#- source
%doc %{_texmfdistdir}/source/latex/nomencl

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar makeindex tex doc source %{buildroot}%{_texmfdistdir}
