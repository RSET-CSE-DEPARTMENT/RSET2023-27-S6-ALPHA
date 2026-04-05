# src/ai/agentic/form_schemas/index.py

from .education.postMatricReal import postMatricReal
from .education.biharStudentCreditCard import biharStudentCreditCard
from .education.biocareWomenScientists import bioCareWomenScientists
from .education.constructionWorkerChildrenAward import constructionWorkerChildrenAward
from .education.hindiInstituteDimapurStipend import hindiInstituteDimapurStipend
from .education.icarJrf import icarJrf
from .education.kanyashreePrakalpa import kanyashreePrakalpa
from .education.meaInternship import meaInternship
from .education.meritAwardsDisabilities import meritAwardsDisabilities
from .education.mukhyamantriYubaYogayog import mukhyamantriYubaYogayog
from .education.nosDisabilities import nosDisabilities
from .education.obcFeeReimbursementUP import obcFeeReimbursementUP
from .education.oecPreMatricAssistance import oecPreMatricAssistance
from .education.postMatricDisabilities import postMatricDisabilities
from .education.researchGrantFaculty import researchGrantFaculty
from .education.sainikSchoolImphal import sainikSchoolImphalScholarship
from .education.saraswatiCycleScheme import saraswatiCycleScheme
from .education.sjpFellowship import sjpFellowship
from .education.tnDisabilityScholarship import tnDisabilityScholarship
from .education.ugcEmeritus import ugcEmeritus


from .housing_shelter.adiDravidarTribalHostels import adiDravidarTribalHostels
from .housing_shelter.banglarAwaasYojana import banglarAwaasYojana
from .housing_shelter.chikitsaPratipoortiYojana import chikitsaPratipoortiYojana
from .housing_shelter.constructionWorkerHousingLoan import constructionWorkerHousingLoan
from .housing_shelter.freeHouseConstructionTribals import freeHouseConstructionTribals
from .housing_shelter.governmentWorkingWomensHostel import governmentWorkingWomensHostel
from .housing_shelter.homesForIntellectuallyImpaired import homesForIntellectuallyImpaired
from .housing_shelter.icdsScheme import icdsScheme
from .housing_shelter.interestSubsidyHomeLoanKSB import interestSubsidyHomeLoanKSB
from .housing_shelter.mapSimplificationProcessUK import mapSimplificationProcessUK
from .housing_shelter.loanAdvanceHouseConstructionTripura import loanAdvanceHouseConstructionTripura
from .housing_shelter.modelMapsResidentialConstructionUK import modelMapsResidentialConstructionUK
from .housing_shelter.mukhyamantriAwasYojnaHP import mukhyamantriAwasYojnaHP
from .housing_shelter.panditDindayalAwasYojanaEBC import panditDindayalAwasYojanaEBC
from .housing_shelter.pratyashaHousingScheme import pratyashaHousingScheme
from .housing_shelter.residentialSchoolForBlinds import residentialSchoolForBlinds
from .housing_shelter.sardarPatelAwasYojanaGJ import sardarPatelAwasYojanaGJ
from .housing_shelter.scHostelMP import scHostelMP
from .housing_shelter.sportsHostelRajasthan import sportsHostelRajasthan
from .housing_shelter.vedVyasHousingConstructionScheme import vedVyasHousingConstructionScheme




from .women_child.asangathiKarmakaarSilaMachineSahayataYojana import asangathitKarmakaarSilaiMachineSahayataYojana
from .women_child.backToLabPostDoctoralFellowship import backToLabPostDoctoralFellowship
from .women_child.bioCareProgramme import bioCareProgramme
from .women_child.ekalNariSammanPensionYojana import ekalNariSammanPensionYojana
from .women_child.iconicMotherAward import iconicMotherAward
from .women_child.incentiveToGirls import incentiveToGirls
from .women_child.kanyashreePrakalpa import kanyashreePrakalpa
from .women_child.marriageAssistanceWidowOrphan import marriageAssistanceWidowOrphan
from .women_child.matruJyothiFinancialAssistance import matruJyothiFinancialAssistance
from .women_child.moovalurMarriageAssistanceScheme1 import moovalurMarriageAssistanceScheme1
from .women_child.mukhyamantriMahilaUtkarshYojana import mukhyamantriMahilaUtkarshYojana
from .women_child.rmewfVocationalTrainingWidow import rmewfVocationalTrainingWidow
from .women_child.saraswatiCycleYojana import saraswatiCycleYojana
from .women_child.savitribaiPhuleSingleGirlPhd import savitribaiPhuleSingleGirlPhd
from .women_child.scGirlRetentionScholarship import scGirlRetentionScholarship
from .women_child.studyInAbroadScheme import studyInAbroadScheme
from .women_child.udyoginiScheme import udyoginiScheme
from .women_child.widowBEdScheme import widowBEdScheme
from .women_child.widowPensionCBOCWWB import widowPensionCBOCWWB
from .women_child.widowPensionWestBengal import widowPensionWestBengal





from .agriculture.cofeeBabyPulperScheme import coffeeBabyPulperScheme
from .agriculture.cofeeDryingYardScheme import coffeeDryingYardScheme
from .agriculture.communityCanningFruitPreservation import communityCanningFruitPreservation
from .agriculture.fishingCraftSubsidyScheme import fishingCraftSubsidyScheme
from .agriculture.krishakBakriPalan import krishakBakriPalan
from .agriculture.krishakUdyamiYojana import krishakUdyamiYojana
from .agriculture.mechanisedBoatSubsidy import mechanisedBoatSubsidy
from .agriculture.mukhyaMantriKrishiSaSajuli import mukhyaMantriKrishiSaSajuli
from .agriculture.nationalFoodSecurityMission import nationalFoodSecurityMission
from .agriculture.outboardMotorSubsidyScheme import outboardMotorSubsidyScheme
from .agriculture.postHarvestMarketingScheme import postHarvestMarketingScheme
from .agriculture.subsidyRIRBirdsUnit import subsidyRIRBirdsUnit
from .agriculture.supplyAgricultureMachineries import supplyAgricultureMachineries
from .agriculture.uttamPashuPuraskar import uttamPashuPuraskar
from .agriculture.vehicleSubsidyScheme import vehicleSubsidyScheme

# Add other schemes later
SCHEMES = {

    # Education
    postMatricReal["scheme_id"]: postMatricReal,
    biharStudentCreditCard["scheme_id"]: biharStudentCreditCard,
    bioCareWomenScientists["scheme_id"]: bioCareWomenScientists,
    constructionWorkerChildrenAward["scheme_id"]: constructionWorkerChildrenAward,
    hindiInstituteDimapurStipend["scheme_id"]: hindiInstituteDimapurStipend,
    icarJrf["scheme_id"]: icarJrf,
    kanyashreePrakalpa["scheme_id"]: kanyashreePrakalpa,
    meaInternship["scheme_id"]: meaInternship,
    meritAwardsDisabilities["scheme_id"]: meritAwardsDisabilities,
    mukhyamantriYubaYogayog["scheme_id"]: mukhyamantriYubaYogayog,
    nosDisabilities["scheme_id"]: nosDisabilities,
    obcFeeReimbursementUP["scheme_id"]: obcFeeReimbursementUP,
    oecPreMatricAssistance["scheme_id"]: oecPreMatricAssistance,
    postMatricDisabilities["scheme_id"]: postMatricDisabilities,
    researchGrantFaculty["scheme_id"]: researchGrantFaculty,
    sainikSchoolImphalScholarship["scheme_id"]: sainikSchoolImphalScholarship,
    saraswatiCycleScheme["scheme_id"]: saraswatiCycleScheme,
    sjpFellowship["scheme_id"]: sjpFellowship,
    tnDisabilityScholarship["scheme_id"]: tnDisabilityScholarship,
    ugcEmeritus["scheme_id"]: ugcEmeritus,


    # Housing & Shelter
    adiDravidarTribalHostels["scheme_id"]: adiDravidarTribalHostels,
    banglarAwaasYojana["scheme_id"]: banglarAwaasYojana,
    chikitsaPratipoortiYojana["scheme_id"]: chikitsaPratipoortiYojana,
    constructionWorkerHousingLoan["scheme_id"]: constructionWorkerHousingLoan,
    freeHouseConstructionTribals["scheme_id"]: freeHouseConstructionTribals,
    governmentWorkingWomensHostel["scheme_id"]: governmentWorkingWomensHostel,
    homesForIntellectuallyImpaired["scheme_id"]: homesForIntellectuallyImpaired,
    icdsScheme["scheme_id"]: icdsScheme,
    interestSubsidyHomeLoanKSB["scheme_id"]: interestSubsidyHomeLoanKSB,
    mapSimplificationProcessUK["scheme_id"]: mapSimplificationProcessUK,
    loanAdvanceHouseConstructionTripura["scheme_id"]: loanAdvanceHouseConstructionTripura,
    modelMapsResidentialConstructionUK["scheme_id"]: modelMapsResidentialConstructionUK,
    mukhyamantriAwasYojnaHP["scheme_id"]: mukhyamantriAwasYojnaHP,
    panditDindayalAwasYojanaEBC["scheme_id"]: panditDindayalAwasYojanaEBC,
    pratyashaHousingScheme["scheme_id"]: pratyashaHousingScheme,
    residentialSchoolForBlinds["scheme_id"]: residentialSchoolForBlinds,
    sardarPatelAwasYojanaGJ["scheme_id"]: sardarPatelAwasYojanaGJ,
    scHostelMP["scheme_id"]: scHostelMP,
    sportsHostelRajasthan["scheme_id"]: sportsHostelRajasthan,
    vedVyasHousingConstructionScheme["scheme_id"]: vedVyasHousingConstructionScheme,


    # Women & Child
    asangathitKarmakaarSilaiMachineSahayataYojana["scheme_id"]: asangathitKarmakaarSilaiMachineSahayataYojana,
    backToLabPostDoctoralFellowship["scheme_id"]: backToLabPostDoctoralFellowship,
    bioCareProgramme["scheme_id"]: bioCareProgramme,
    ekalNariSammanPensionYojana["scheme_id"]: ekalNariSammanPensionYojana,
    iconicMotherAward["scheme_id"]: iconicMotherAward,
    incentiveToGirls["scheme_id"]: incentiveToGirls,
    marriageAssistanceWidowOrphan["scheme_id"]: marriageAssistanceWidowOrphan,
    matruJyothiFinancialAssistance["scheme_id"]: matruJyothiFinancialAssistance,
    moovalurMarriageAssistanceScheme1["scheme_id"]: moovalurMarriageAssistanceScheme1,
    mukhyamantriMahilaUtkarshYojana["scheme_id"]: mukhyamantriMahilaUtkarshYojana,
    rmewfVocationalTrainingWidow["scheme_id"]: rmewfVocationalTrainingWidow,
    saraswatiCycleYojana["scheme_id"]: saraswatiCycleYojana,
    savitribaiPhuleSingleGirlPhd["scheme_id"]: savitribaiPhuleSingleGirlPhd,
    scGirlRetentionScholarship["scheme_id"]: scGirlRetentionScholarship,
    studyInAbroadScheme["scheme_id"]: studyInAbroadScheme,
    udyoginiScheme["scheme_id"]: udyoginiScheme,
    widowBEdScheme["scheme_id"]: widowBEdScheme,
    widowPensionCBOCWWB["scheme_id"]: widowPensionCBOCWWB,
    widowPensionWestBengal["scheme_id"]: widowPensionWestBengal,


    # Agriculture
    coffeeBabyPulperScheme["scheme_id"]: coffeeBabyPulperScheme,
    coffeeDryingYardScheme["scheme_id"]: coffeeDryingYardScheme,
    communityCanningFruitPreservation["scheme_id"]: communityCanningFruitPreservation,
    fishingCraftSubsidyScheme["scheme_id"]: fishingCraftSubsidyScheme,
    krishakBakriPalan["scheme_id"]: krishakBakriPalan,
    krishakUdyamiYojana["scheme_id"]: krishakUdyamiYojana,
    mechanisedBoatSubsidy["scheme_id"]: mechanisedBoatSubsidy,
    mukhyaMantriKrishiSaSajuli["scheme_id"]: mukhyaMantriKrishiSaSajuli,
    nationalFoodSecurityMission["scheme_id"]: nationalFoodSecurityMission,
    outboardMotorSubsidyScheme["scheme_id"]: outboardMotorSubsidyScheme,
    postHarvestMarketingScheme["scheme_id"]: postHarvestMarketingScheme,
    subsidyRIRBirdsUnit["scheme_id"]: subsidyRIRBirdsUnit,
    supplyAgricultureMachineries["scheme_id"]: supplyAgricultureMachineries,
    uttamPashuPuraskar["scheme_id"]: uttamPashuPuraskar,
    vehicleSubsidyScheme["scheme_id"]: vehicleSubsidyScheme,
}



