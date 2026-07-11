%global tl_name nomencl
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	5.6
Release:	%{tl_revision}.1
Summary:	Produce lists of symbols as in nomenclature
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/nomencl
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/nomencl.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/nomencl.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/nomencl.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Produces lists of symbols using the capabilities of the MakeIndex
program.

