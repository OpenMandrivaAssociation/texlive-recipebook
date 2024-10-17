Name:		texlive-recipebook
Version:	37026
Release:	2
Summary:	Typeset 5.5" x 8" recipes for browsing or printing
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/recipebook
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/recipebook.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/recipebook.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a LaTeX2e class for typesetting recipes. It is designed
for typesetting one or two recipes per page, with dimensions of
5.5" x 8.5". The hyperlinked table of contents (ToC) and page
numbers make browsing recipes convenient, and the pages can be
joined together or printed two per sheet to normal letterpaper
easily. The size was chosen to work in half-page 3-ring binder
cover sheets.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/recipebook
%doc %{_texmfdistdir}/doc/latex/recipebook

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
