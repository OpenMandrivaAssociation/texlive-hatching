# revision 23818
# category Package
# catalog-ctan /graphics/metapost/contrib/macros/hatching
# catalog-date 2006-12-17 23:49:42 +0100
# catalog-license pd
# catalog-version 0.11
Name:		texlive-hatching
Version:	0.11
Release:	3
Summary:	MetaPost macros for hatching interior of closed paths
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/metapost/contrib/macros/hatching
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hatching.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hatching.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar metapost doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.11-2
+ Revision: 752524
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.11-1
+ Revision: 718605
- texlive-hatching
- texlive-hatching
- texlive-hatching
- texlive-hatching

