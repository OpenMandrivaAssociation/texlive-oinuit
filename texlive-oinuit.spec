# revision 28668
# category Package
# catalog-ctan /language/inuktitut/oinuit
# catalog-date 2012-06-16 10:52:26 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-oinuit
Version:	20120616
Release:	5
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
The package provides a set of Lambda (Omega LaTeX) typesetting
tools for the Inuktitut language. Five different input methods
are supported and with the necessary fonts are also provided.

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
%{_texmfdistdir}/omega/otp/oinuit/Ninuit2uni.otp
%{_texmfdistdir}/omega/otp/oinuit/Qinuit2uni.otp
%{_texmfdistdir}/omega/otp/oinuit/inuitscii.otp
%{_texmfdistdir}/tex/lambda/oinuit/litcmr.fd
%{_texmfdistdir}/tex/lambda/oinuit/litenc.def
%{_texmfdistdir}/tex/lambda/oinuit/oinuit.sty
%doc %{_texmfdistdir}/doc/fonts/oinuit/README.1ST
%doc %{_texmfdistdir}/doc/fonts/oinuit/README.TEXLIVE
%doc %{_texmfdistdir}/doc/fonts/oinuit/Table.eps
%doc %{_texmfdistdir}/doc/fonts/oinuit/book.tex
%doc %{_texmfdistdir}/doc/fonts/oinuit/inuit.tex
%doc %{_texmfdistdir}/doc/fonts/oinuit/taqtu.tex
#- source
%doc %{_texmfdistdir}/source/lambda/oinuit/oinuit.dtx
%doc %{_texmfdistdir}/source/lambda/oinuit/oinuit.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts omega tex doc source %{buildroot}%{_texmfdistdir}
