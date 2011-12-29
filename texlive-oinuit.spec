# revision 15878
# category Package
# catalog-ctan /language/inuktitut/oinuit
# catalog-date 2007-02-23 22:01:12 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-oinuit
Version:	20070223
Release:	1
Summary:	LaTeX Support for the Inuktitut Language
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/inuktitut/oinuit
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/oinuit.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/oinuit.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/oinuit.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The oinuit system is a set of Lambda (Omega LaTeX) typesetting
tools for the Inuktitut language. The oinuit package supports
five different input methods and is bundled with the necessary
fonts.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/map/dvips/oinuit/oinuit.map
%{_texmfdistdir}/fonts/ofm/public/oinuit/OInuit.ofm
%{_texmfdistdir}/fonts/ofm/public/oinuit/OInuitb.ofm
%{_texmfdistdir}/fonts/ofm/public/oinuit/OInuitbo.ofm
%{_texmfdistdir}/fonts/ofm/public/oinuit/OInuito.ofm
%{_texmfdistdir}/fonts/ovf/public/oinuit/OInuit.ovf
%{_texmfdistdir}/fonts/ovf/public/oinuit/OInuitb.ovf
%{_texmfdistdir}/fonts/ovf/public/oinuit/OInuitbo.ovf
%{_texmfdistdir}/fonts/ovf/public/oinuit/OInuito.ovf
%{_texmfdistdir}/fonts/tfm/public/oinuit/Inuit.tfm
%{_texmfdistdir}/fonts/tfm/public/oinuit/Inuitb.tfm
%{_texmfdistdir}/fonts/tfm/public/oinuit/Inuitbo.tfm
%{_texmfdistdir}/fonts/tfm/public/oinuit/Inuito.tfm
%{_texmfdistdir}/fonts/type1/public/oinuit/Inuit.pfb
%{_texmfdistdir}/fonts/type1/public/oinuit/Inuitb.pfb
%{_texmfdistdir}/fonts/type1/public/oinuit/Inuitbo.pfb
%{_texmfdistdir}/fonts/type1/public/oinuit/Inuito.pfb
%{_texmfdistdir}/fonts/type1/public/oinuit/cmssbxo10.pfb
%{_texmfdistdir}/omega/ocp/oinuit/Ninuit2uni.ocp
%{_texmfdistdir}/omega/ocp/oinuit/Qinuit2uni.ocp
%{_texmfdistdir}/omega/ocp/oinuit/inuitscii.ocp
%{_texmfdistdir}/tex/lambda/oinuit/oinuit.sty
%doc %{_texmfdistdir}/doc/fonts/oinuit/README.1ST
%doc %{_texmfdistdir}/doc/fonts/oinuit/examples/book.tex
%doc %{_texmfdistdir}/doc/fonts/oinuit/examples/taqtu.tex
#- source
%doc %{_texmfdistdir}/source/lambda/oinuit/oinuit.dtx
%doc %{_texmfdistdir}/source/lambda/oinuit/oinuit.ins
%doc %{_texmfdistdir}/source/lambda/oinuit/oinuit.sty

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts omega tex doc source %{buildroot}%{_texmfdistdir}
