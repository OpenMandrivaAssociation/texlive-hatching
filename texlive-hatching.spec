Name:		texlive-hatching
Version:	0.11
Release:	1
Summary:	MetaPost macros for hatching interior of closed paths
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/metapost/contrib/macros/hatching
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hatching.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hatching.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The file hatching.mp contains a set of MetaPost macros for
hatching interior of closed paths. Examples of usage are
included.

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
