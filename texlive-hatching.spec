Name:		texlive-hatching
Version:	23818
Release:	2
Summary:	MetaPost macros for hatching interior of closed paths
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/metapost/contrib/macros/hatching
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hatching.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hatching.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The file hatching.mp contains a set of MetaPost macros for
hatching interior of closed paths. Examples of usage are
included.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/metapost/hatching/hatching.mp
%doc %{_texmfdistdir}/doc/metapost/hatching/README
%doc %{_texmfdistdir}/doc/metapost/hatching/htchuse.mp
%doc %{_texmfdistdir}/doc/metapost/hatching/htchuse_.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar metapost doc %{buildroot}%{_texmfdistdir}
